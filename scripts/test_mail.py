from django.core.mail import EmailMessage


def run():
    EmailMessage(
        subject='Subject here',
        body='Here is the message.',
        to=['marco.ponce@rama-ws.com'],
    ).send()