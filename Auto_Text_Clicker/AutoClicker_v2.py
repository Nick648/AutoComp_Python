import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key
from colorama import Fore, Style, init

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
CYAN = Fore.LIGHTCYAN_EX
RESET = Style.RESET_ALL

# Keys
autoclick_key = None
mechanic_click_key = None
# autoclick_key = KeyCode(char='s')

# Bool
auto_clicking = False
mechanic_clicking = False
exiting = False

# Count
count_auto_click = 0
count_mechanic_click = 0
count_click_time = 1  # Number of clicks at a time

mouse = Controller()


def error_out(text: str) -> None:  # Red text output
    print(RED + text + RESET, sep='')


def done_out(text: str) -> None:  # Green text output
    print(GREEN + text + RESET, sep='')


def yellow_out(text: str) -> None:  # Yellow text output
    print(YELLOW + text + RESET, sep='')


# Selecting the automatic clicker launch key (on/off)
def choose_keycode_1(key) -> None:
    if key == Key.enter:
        print('Ok, the auto clicker key is not selected.')
        exit()
    print(f"The automatic clicker key is selected: {key=}; Type = {type(key)}")
    global autoclick_key
    autoclick_key = key
    exit()


# Selecting the mechanical clicker launch key (press for use)
def choose_keycode_2(key) -> None:
    if key == Key.enter:
        print('Ok, The mechanical clicker key is not selected.')
        exit()
    print(f"The mechanical clicker key is selected: {key=}; Type = {type(key)}")
    global mechanic_click_key
    mechanic_click_key = key
    exit()


def choose_click_symbol() -> None:
    print("You need to select two keys responsible for the clicker.\nIf you don't need any key, just press Enter.\n")

    with Listener(on_press=choose_keycode_1) as listener:
        print(MAGENTA + "\tSelect the key responsible for the clicker(on/off): ")
        listener.join()
    with Listener(on_press=choose_keycode_2) as listener:
        print(MAGENTA + "\tSelect the key responsible for the clicker(press for use): ")
        listener.join()
    if autoclick_key is None and mechanic_click_key is None:
        error_out("\n\tYou have not selected the keys to launch the clicker!")
        exit()
    return


def clicker() -> None:
    while not exiting:
        if auto_clicking:
            mouse.click(Button.left, 1)
            global count_auto_click
            # mouse.click(Button.left, count_click_time)
            # count_auto_click += count_click_time
            count_auto_click += 1
            time.sleep(0.1)
        elif mechanic_clicking:
            mouse.click(Button.left, 1)
            global count_mechanic_click
            count_mechanic_click += 1
            time.sleep(0.1)


def func_exiting_app() -> None:
    app_info = f"\n\tProcessed information:\n" \
               f"Number of automatic clicks = {count_auto_click};\n" \
               f"Number of mechanical clicks = {count_mechanic_click};\n" \
               f"Total number of clicks = {count_auto_click + count_mechanic_click}\n" \
               f"\tThx for using!"
    done_out(app_info)
    exit()


# The function of checking keystrokes for the main listener
def toggle_event(key) -> None:
    if key == autoclick_key:
        global auto_clicking
        auto_clicking = not auto_clicking
    elif key == mechanic_click_key and auto_clicking is False:
        global mechanic_clicking
        mechanic_clicking = True
    elif key == Key.esc:
        global exiting
        exiting = True
        func_exiting_app()


# The function of checking the released keys for the main listener
def on_release(key) -> None:
    if key == mechanic_click_key:
        global mechanic_clicking
        mechanic_clicking = False


def main() -> None:
    choose_click_symbol()
    print()
    clicking_thread = threading.Thread(target=clicker, daemon=True)
    clicking_thread.start()

    with Listener(on_press=toggle_event, on_release=on_release) as listener:
        info_text = CYAN + f"\n\tControl keys:\n" \
                           f"Automatic clicker key = {autoclick_key};\n" \
                           f"Mechanical clicker key = {mechanic_click_key};\n" \
                           f"To exit, press 'Esc'. Enjoy using it!" + RESET
        print(info_text)
        listener.join()


if __name__ == '__main__':
    hello_text = YELLOW + " The Clicker program " + RESET
    print("\n", "{:*^75}".format(hello_text), "\n")
    main()
