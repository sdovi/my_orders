from django.conf import settings
from twilio.rest import Client

from eskiz_sms import EskizSMS


def send_message(phone_number, code):
    client = EskizSMS(settings.ESKIZ_USERNAME, settings.ESKIZ_PASSWORD)
    if phone_number.startswith('+998') or phone_number.startswith('998'):
        client.send_sms(phone_number, f"GTRobot uchun tasdiqlash kodi: {code}")
    else:
        raise Exception("Invalid phone number")


def send_message_via_whatsapp(phone_number, code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=f"whatsapp:{phone_number}",
        from_=f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}",
        body=f"*{code}* is your verification code. For your security, do not share this code."
    )
    return message