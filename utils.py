# utils.py
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

sender_email = os.environ.get('GMAIL')
app_password = os.environ.get('GMAIL_APP_PASSWORD')

# Shared state variables
recipient_email = ''
email_body = ''
email_subject = ''

@tool
def update_body(content: str) -> str:
   '''  
   Update the current email body based on the new content
   Args:
        content : new document
    Return:
        str : New content
   '''
   global email_body
   email_body = content
   return f"Document has been updated successfully! The current email content is:\n {email_body}"

@tool
def update_subject(content: str) -> str:
   '''  
   Update the current email subject based on the new content
   Args:
        content : new subject
    Return:
        str : New content
   '''
   global email_subject
   email_subject = content
   return f"Subject has been updated successfully! The current email subject is:\n {email_subject}"

@tool
def update_recipient(content: str) -> str:
   '''  
   Update the current email recipient based on the new content
   Args:
        content : new recipient
    Return:
        str : New content
   '''
   global recipient_email
   recipient_email = content
   return f"Recipient has been updated successfully! The current email content is:\n {recipient_email}"

@tool
def show_email():
    ''' 
    Show the current email
    Args:
        None, call all the varaibles
    Return:
        str : The full current email
    '''
    global sender_email, recipient_email, email_body, email_subject

    current_email = f"""
    From: {sender_email if len(sender_email) > 0 else 'empty'}
    To: {recipient_email if len(recipient_email) > 0 else 'empty'}
    Subject: {email_subject if len(email_subject) > 0 else 'empty'}
    {email_body if len(email_body) > 0 else 'empty'}
    """

    return current_email
 

@tool
def save_draft(filename: str) -> str:
    """
    Save the current email information (recipient, subject, body) to a text file and finish the process.
    Args:
        filename (str): Name for the text file (without extension or with .txt).
    Return:
        str : Status message
    """
    global sender_email, email_subject, email_body, recipient_email
    
    if not filename.endswith('.txt'):
        filename += '.txt'

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"From: {sender_email}\n")
            file.write(f"To: {recipient_email}\n")
            file.write(f"Subject: {email_subject}\n")
            file.write(f"{email_body}")
        return f"Email has been saved successfully to '{filename}'."
    except Exception as e:
        return f"An error occurred while saving the email: {e}"

@tool
def send_email():

    '''  
    Send the email
    Args:
        None : Using global varaibles
    Return:
        str : Status message
    '''
    global sender_email, recipient_email, email_subject, email_body

    if len(sender_email) <= 0:
        return "Sender email address is empty"
    if len(recipient_email) <= 0:
        return "Reciever email address is empty"
    if len(email_subject) <= 0:
        return "Email subject is empty"
    if len(email_body) <= 0:
        return "Email body is empty"

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = email_subject
    msg.set_content(email_body)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending message: {e}"

