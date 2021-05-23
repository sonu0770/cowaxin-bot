import requests
from twilio.rest import Client
import time

def sms(message):
    account_sid = 'ACc3ab9992d059906fe2bba5b81a9103a9'
    auth_token = '9665c7f9c7393354b4b94cf4a2b31615'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_='+12158263290',
            to='+917489809756'
        )

    print(message.sid)


url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=455118&date=24-05-2021'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
print("BOT Running......")
while True:
    time.sleep(30)
    result = requests.get(url, headers=headers).json()
    l1 = result["sessions"]
    l2 = l1[2]
    slot1 = l2['available_capacity_dose1']
    slot2 = l2['available_capacity']
    if slot1 > 0 or slot2 > 0:
        message = "Slot available " + str(slot1) +" "+ str(slot2)
        print(message)
        sms(message)
