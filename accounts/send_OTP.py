from twilio.rest import Client
from django.conf import settings


def send_sms_code(phone_number, code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body=f"Your verification code is {code}",
        from_=settings.TWILIO_FROM_NUMBER,
        to=f'{phone_number}'
    )

    print(message.sid)
