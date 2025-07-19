
# MailFast Agent

AI-powered chat assistant that help **compose**, **edit** and **send emails**

## Description

MailFast is an AI-powered email assistant that helps users manage emails through ongoing conversation. It is designed to streamline the email workflow with a simple and intuitive chat interface.

-  **Compose** complete email content from prompts
-  **Edit** existing email drafts
-  **Update** the recipient and subject on the fly
-  **Show** the full email content
-  **Send** emails directly via your configured Gmail account

## Work Flow
MailFast is built using LangGraph’s stateful agent architecture, which orchestrates how user input flows through the system. The graph below illustrates the agent logic:

<img width="260" height="273" alt="graph" src="https://github.com/user-attachments/assets/d6c802d5-6283-4cf6-b21b-0f049607b3ba" />


## Getting Started

### Installation

#### **1. Clone the repository:**

```bash
git clone https://github.com/minhman21032004/MailFast.git
cd MailFast
```

#### **2. Create virtual environment and install dependencies:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

#### **3. Setup environment variables:**
```bash
# Gmail configuration
GMAIL="your-gmail@gmail.com"
GMAIL_APP_PASSWORD="your-gmail-app-password"

# Azure OpenAI configuration
OPENAI_API_KEY="your-azure-openai-key"
OPENAI_API_VERSION="2024-05-01"
OPENAI_API_ENDPOINT="https://your-resource-name.openai.azure.com/"
DEPLOYMENT_NAME="your-deployment-name"
```
- To generate a Gmail App Password, follow this quick guide (Youtube): 
[How to Generate App Passwords in Google](https://youtu.be/MkLX85XU5rU?si=K8GlDm4yrTTLqovw)

- Make sure your Azure OpenAI deployment name and version match the actual deployment you set up on the Azure portal.


### How to run:
Run the streamlit app :
```bash
streamlit run main.py
```

### Demo application:
+ **Create Email:**
  
<img width="1015" height="910" alt="demo_1" src="https://github.com/user-attachments/assets/04256b42-df67-4791-9003-5eb62e04e644" />

+ **Edit Email:**

<img width="952" height="561" alt="demo_2" src="https://github.com/user-attachments/assets/ed674497-272d-4478-b728-92e43f65320c" />

+ **Update subject, recipient:**

<img width="976" height="711" alt="demo_3" src="https://github.com/user-attachments/assets/1575a0e2-7ab1-4802-8b2c-7b972f765be7" />

+ **Show Email:**
  
<img width="925" height="813" alt="demo_4" src="https://github.com/user-attachments/assets/caa34d18-40d0-4493-8b3a-8d9ec574729c" />

+ **Send Email:**

<img width="983" height="900" alt="demo_5" src="https://github.com/user-attachments/assets/4176020e-6ec3-48e8-bcaa-79c644302f05" />

+ **Result:**

<img width="1537" height="672" alt="demo_6" src="https://github.com/user-attachments/assets/05fda160-6c45-41c3-b376-6fdba5f1f549" />

### Framework used:
+ LangChain
+ LangGraph
+ AzureOpenAI
+ Streamlit

## Created By :
Manbell
minhman210304@gmail.com
