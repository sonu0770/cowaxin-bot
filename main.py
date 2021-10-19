#adding libraries
import requests
from twilio.rest import Client
import time

def sms(message):
    account_sid = '<YOUR-SID>'
    auth_token = '<YOUR-TOKEN>'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_='<YOUR_TWILIO_NO.>',
            to='+91XXXXXXXXXX'
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
