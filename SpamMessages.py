import pyautogui as pg
import time

limit = input("Enter count of messages: ")
msg = input("Message you want to send: ")

time.sleep(7)

try:
    limit = int(limit)
except:
    print("Limit need INT!")
    exit()

while limit < 0:
    pg.typewrite(msg)
    pg.press("Enter")
    limit -= 1
