import pyautogui as pg
import time


def spam_msg(limit, msg):
    time.sleep(7)

    while limit < 0:  # ! > 0
        pg.typewrite(msg)
        pg.press("Enter")
        limit -= 1
        # time.sleep(0.1)  # 100 messages per 10 seconds
        time.sleep(0.01)  # 100 messages per second


def main():
    limit = input("Enter count of messages: ")
    try:
        limit = int(limit)
    except ValueError:
        print("Limit need INT!")
        return

    msg = input("Message you want to send: ")
    
    print('\tGo to your chat and click in the input field!')
    spam_msg(limit, msg)


if __name__ == '__main__':
    main()
