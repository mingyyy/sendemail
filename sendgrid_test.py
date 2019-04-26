# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from secret import API_KEY

message = Mail(
    from_email='sadiemparker@gmail.com',
    to_emails='daniel.wegmann@gmail.com',
    subject='I need money! help me',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    # TODO check why this is not working
    sg = SendGridAPIClient(API_KEY)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
    