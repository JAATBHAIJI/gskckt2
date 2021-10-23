from twilio.rest import Client

account_sid = "ACd9f05f561af0d17a451bea6008099cdf"
auth_token = "3a8d8ea837bfed6309a1ff357cadf8f9"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+918433120646",
    from_="+12512921406",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)
