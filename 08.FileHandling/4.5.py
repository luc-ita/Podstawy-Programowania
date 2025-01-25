import re

file = 'email.txt'

with open(file, 'r') as f:
    email_content = f.read()

def email_sender(email_content):
    sender_match = re.search('From: .*<(.*)>', email_content)
    return sender_match.group(1)


def email_recipient(email_content):
    recipient_match = re.search('To: .*<(.*)>', email_content)
    return recipient_match.group(1)


def email_subject(email_content):
    subject_match = re.search('Subject: (.*)', email_content)
    return subject_match.group(1)


def email_body(email_content):
    body_match = re.search(r"\n\n(.*)", email_content, re.DOTALL)
    return body_match.group(1).strip()



print(f'Sender email: {email_sender(email_content)}')
print(f'Recipient email: {email_recipient(email_content)}')
print(f'Subject: {email_subject(email_content)}')
print(f'Body: \n{email_body(email_content)}')
