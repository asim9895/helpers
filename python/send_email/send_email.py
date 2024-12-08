import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email_add = ""
passw = ""
host = "smtp.gmail.com"
port = 587
html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = ''
email['subject'] = 'First email for test'
email.set_content(html.substitute({'name': "John Doe", 'age': 18}), 'html')


def simple_email(email_address: str, password: str, email_message):
    server = smtplib.SMTP(host=host, port=port)
    server.ehlo()
    server.starttls()
    server.login(email_address, password)
    server.send_message(email_message)
    server.quit()


simple_email(email_add, passw, email)
