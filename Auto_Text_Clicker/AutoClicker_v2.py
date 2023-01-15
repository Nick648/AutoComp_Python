import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


def choose_keycode(key):
    print(key, type(key))
    return key


def choose_click_symbol():
    sym = input('Enter click key: ')

    with Listener(on_press=choose_keycode) as listener:
        listener.join()


# toggle_key = KeyCode(char='s')
toggle_key = choose_click_symbol()
clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.1)


def toggle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking


def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()


if __name__ == '__main__':
    main()
