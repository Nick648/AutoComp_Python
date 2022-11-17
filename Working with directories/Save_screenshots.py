import time
import os
from PIL import ImageGrab
import datetime
import keyboard
from colorama import Fore, Style

# colorama.init()
# Const module colorama
GREEN = Fore.LIGHTGREEN_EX
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

# Consts for time and date
today = datetime.datetime.today()
date_y, date_m, date_d = today.year, today.month, today.day
# time_h, time_m, time_s = today.hour, today.minute, today.second

# Name of directory
CUR_DIR_FILE = os.path.abspath(__file__)  # With name file.py
CUR_DIR = os.path.dirname(os.path.abspath(__file__))  # Without name file.py
NAME_DIR = f'Screenshots {date_d}_{date_m}_{date_y}'
WAY_DIR = os.path.join(CUR_DIR, NAME_DIR)


# Creating a folder
def create_dir():
    if not os.path.exists(WAY_DIR):  # Creating a folder for images
        os.mkdir(WAY_DIR)


# Reading the clipboard
def reading_clipboard():
    print(YELLOW + "=" * 30 + RESET)
    old_copy = None
    count = 0
    while True:
        copy_im = ImageGrab.grabclipboard()
        if old_copy != copy_im and copy_im is not None:
            count += 1
            old_copy = copy_im
            time_now = datetime.datetime.today()
            time_h, time_m, time_s = time_now.hour, time_now.minute, time_now.second
            name_screen = os.path.join(WAY_DIR, f'Screen {count}  ({time_h}-{time_m}-{time_s}).png')
            print(copy_im, type(copy_im))
            print(f'\t{GREEN + "Copy Done!" + RESET} Save as: {name_screen}')
            copy_im.save(name_screen, 'PNG')
            print(YELLOW + "=" * 30 + RESET)
        if keyboard.is_pressed('Esc'):
            break

        time.sleep(1)

    print(f'\tTotal screenshots: {count}')


def main():
    create_dir()
    reading_clipboard()


if __name__ == '__main__':
    greeting = '''
        A program for saving screenshots taken. Click for:
        Esc - for early exit;
        Enjoy using it!
        '''
    print(YELLOW + greeting + RESET)
    main()
