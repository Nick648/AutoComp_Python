# pip install twilio
from twilio.rest import Client
import os


def sending_sms(text='SMS use twilio...', receiver='+79265439393'):
    try:
        account_sid = os.getenv('SID')
        auth_token = os.getenv('AUTH_TOKEN')

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=text,
            from_='NUMBER_TWILIO',
            to=receiver
        )

        return 'The message was successfully sent!'
    except Exception as ex:
        print(f'Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')
        return 'Something was wrong... :('


def main():
    text = input('Please enter your message: ')
    receiver = os.getenv('RECEIVER_PHONE')
    ans = sending_sms(text=text, receiver=receiver)
    print(f'\t>>> {ans}')


if __name__ == '__main__':
    main()
