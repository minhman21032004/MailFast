import os
from typing import Annotated, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage, SystemMessage
from langchain_openai import AzureChatOpenAI
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages

from utils import (
    update_body, update_subject, update_recipient,
    save_draft, show_email, send_email
)

from utils import recipient_email, email_subject, email_body

#Load env
api_version = os.environ.get("OPENAI_API_VERSION")
api_endpoint = os.environ.get("OPENAI_API_ENDPOINT")
api_key = os.environ.get("OPENAI_API_KEY")
deployment_name = os.environ.get("DEPLOYMENT_NAME")

tools = [update_body, update_subject, update_recipient, save_draft, show_email, send_email]
tools_dict = {tool.name: tool for tool in tools}


system_prompt = f"""
    You are MailFast, a helpful emailing assistant. You are going to help the user write draft, update, save then email.
    I have made tool for you that will help:
    - If the user wants to create or update body of the email, use the 'update_body'.
    - If the user wants to create or update subject of the email, use the 'update_subject'.
    - If the user wants to create or update recipent of the email, use the 'update_recipient'. If there are more than 1 recipent, you may have to send the email multiple times
    - If the user wants to save and finish, you need to use the 'save_draft' tool.
    - If the user want to send the email, use the 'send_email' tool
    - Make sure to show the current email after create, update step with 'show_email' tool
    
    The current recipent is: {recipient_email}
    The current subject content is: {email_subject}
    The current body content is:{email_body}
    """

#Define Agent
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


def should_continue(state: AgentState):
    result = state['messages'][-1]
    return hasattr(result, 'tool_calls') and len(result.tool_calls) > 0

llm = AzureChatOpenAI(
    api_version=api_version,
    azure_endpoint=api_endpoint,
    api_key=api_key,
    azure_deployment=deployment_name
).bind_tools(tools)

def call_llm(state: AgentState) -> AgentState:
    messages = [SystemMessage(content=system_prompt)] + list(state['messages'])
    result = llm.invoke(messages)
    return {'messages': [result]}

def tool_call(state: AgentState) -> AgentState:
    tool_calls = state['messages'][-1].tool_calls
    results = []

    for t in tool_calls:
        if t['name'] not in tools_dict:
            content = f"Tool '{t['name']}' not found."
        else:
            content = tools_dict[t['name']].invoke(t['args'])
        results.append(ToolMessage(tool_call_id=t['id'], name=t['name'], content=str(content)))

    state['messages'] = state['messages'] + results
    return state

#Build workflow
def create_app():
    G = StateGraph(AgentState)
    G.add_node('llm', call_llm)
    G.add_node('tools_node', tool_call)

    G.add_conditional_edges(
        source='llm',
        path=should_continue,
        path_map={
            True: 'tools_node',
            False: END
        }
    )

    G.add_edge('tools_node', 'llm')
    G.set_entry_point('llm')
    return G.compile()
