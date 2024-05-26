from twilio.rest import Client

client = Client(
    "ACa09257eb5d916af2ebd5614a4d0caac4",
    "5fde81986b18212b45ecdeb2543c28e5"
)
phone_number = "whatsapp:+14155238886"


verification = client.messages.create(
    to="whatsapp:+998948962660",
    from_=phone_number,
    body="*21415* is your verification code. For your security, do not share this code."
)
print(verification)