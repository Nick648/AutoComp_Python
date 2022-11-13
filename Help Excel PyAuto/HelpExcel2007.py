import time
import pyautogui as pg
import keyboard as key
import os
from colorama import Fore, Back, Style

# colorama.init()

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

# Const directory
CUR_DIR = os.path.dirname(os.path.abspath(__file__))  # Without name file.py
DATA_DIR = os.path.join(CUR_DIR, 'data')


def exi_t(farewell="Goodbye!\nThx for using our program!"):  # Exit program
    farewell = GREEN + farewell + RESET
    print('\n' + farewell)
    exit()


def print_info_bl(bl):
    print(GREEN, end='')
    print(bl)
    print(RESET, end='')


def only_pg():
    while True:
        if key.is_pressed('Ctrl'):
            time.sleep(0.1)
            pg.click(button='right')
            pg.move(80, -80, duration=0.15)  # Format cells
            time.sleep(0.15)
            pg.click()
            time.sleep(0.15)
            pg.move(-240, 15, duration=0.15)  # Combining
            time.sleep(0.15)
            pg.click()
            time.sleep(0.15)
            pg.move(375, 180, duration=0.15)  # Button ok
            time.sleep(0.15)
            pg.click()

        if key.is_pressed('Esc'):
            break


def search_loc_pic():  # Нахождение по скринам
    while True:
        if key.is_pressed('Ctrl'):
            time.sleep(0.1)
            pg.click(button='right')
            time.sleep(0.15)
            name_file = os.path.join(DATA_DIR, 'format_cells.png')
            bl = pg.locateOnScreen(name_file, confidence=0.9)
            # print_info_bl(bl)
            # bl = pg.locateCenterOnScreen('data/excel/format_cells.png')
            # pg.moveTo(bl)
            pg.click(bl)
            if not bl:
                print(RED + "Not found format_cells.png!" + RESET)
                continue

            time.sleep(0.2)
            name_file = os.path.join(DATA_DIR, 'combining.png')
            bl = pg.locateOnScreen(name_file, confidence=0.75)
            pg.click(bl)
            if not bl:
                print(RED + "Not found combining.png!" + RESET)
                continue

            name_file = os.path.join(DATA_DIR, 'button_ok.png')
            bl = pg.locateOnScreen(name_file, confidence=0.9)
            time.sleep(0.15)
            pg.click(bl)
            if not bl:
                print(RED + "Not found button_ok.png!" + RESET)
                continue

        if key.is_pressed('Esc'):
            break


if __name__ == "__main__":
    greeting = '''
    A program for quickly combining cells in Excel 2007.
    Click for:
    Ctrl - use program;
    Esc - for early exit;
    Enjoy using it!
    '''
    greeting = YELLOW + greeting + RESET
    print("*" * 30, greeting, "*" * 30, sep='\n')
    # only_pg()
    search_loc_pic()
    exi_t()
