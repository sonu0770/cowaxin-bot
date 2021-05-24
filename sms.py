from twilio.rest import Client
import time
print("started")
for i in range(0,8):
    if i == 6:
        account_sid = 'ACc3ab9992d059906fe2bba5b81a9103a9'
        auth_token = '9665c7f9c7393354b4b94cf4a2b31615'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body='This is the ship that made the Kessel Run in fourteen parsecs?',
            from_='+12158263290',
            to='+917489809756'
        )

        print(message.sid)
    time.sleep(30)
