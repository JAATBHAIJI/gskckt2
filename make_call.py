from twilio.rest import Client

account_sid = "ACd9f05f561af0d17a451bea6008099cdf"
auth_token = "d5222acb68863105839cc0ad603af925"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+918433120646",
    from_="+12512921406",
    url="https://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
