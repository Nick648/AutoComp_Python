import keyboard
import sys
import os
import keyword

from colorama import Fore, Style

# colorama.init()

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
CYAN = Fore.LIGHTCYAN_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
RESET = Style.RESET_ALL

# Consts
FULL_WAY = os.getcwd()  # == CUR_DIR
HOME_DIR = os.path.expanduser('~')
DESKTOP_DIR = os.path.expanduser('~') + r'\Desktop'
CUR_DIR = os.path.abspath(os.curdir)
OS_DIR = os.curdir  # .
CUR_DIR_FILE = os.path.abspath(__file__)  # With name file.py


def display_env_vars():
    # Создаём цикл, чтобы вывести все переменные среды
    print(CYAN + '\t« The keys and values of all environment variables »' + RESET)
    for key in os.environ:
        print(f'{key} => {os.environ[key]}')

    print(MAGENTA + f'\tThe value of USERNAME is: {os.environ["USERNAME"]}' + RESET)
    os.environ["DATA"] = '20.11.22'
    print(f'\tNew Var = {os.environ["DATA"]}')


def out_consts():  # Вывод констант
    print(GREEN, '*' * 50, RESET, sep='')
    print(f"FULL_WAY: {FULL_WAY}; \nCUR_DIR: {CUR_DIR}; "
          f"\nCUR_DIR_FILE: {CUR_DIR_FILE}; \nOS_DIR: {OS_DIR}"
          f"\nHOME_DIR: {HOME_DIR}; \nDESKTOP_DIR: {DESKTOP_DIR}")
    print(GREEN, '*' * 50, RESET, sep='')


def check_keyboard_keys():  # Запись и вывод нажатых клавиш
    print(YELLOW, end='')
    print("Запись нажатых клавиш, для остановки нажмите: 'Esc'")
    print("Запись...")
    print(RESET, end='')
    recorded_events = keyboard.record("esc")
    print(GREEN + "\nDone!\n" + RESET, sep='')
    print(f"recorded_events: {recorded_events}")
    # print(keyboard.read_hotkey())  # Вывод сочетаний клавиш (х1)
    print(f"sys.argv: {sys.argv}")  # ['C:/Users/User/PycharmProjects/PythonProject/Revenge/CountWordsTXT.py']


def out_keywords():
    print('Keywords')
    print(keyword.kwlist)


if __name__ == '__main__':
    hello = YELLOW + " Module os and keyboard and keyword" + RESET
    print("\n", "{:*^80}".format(hello), "\n", sep='')
    out_consts()
    display_env_vars()
    # check_keyboard_keys()
    # out_keywords()
