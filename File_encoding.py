import sys
import locale
import os
from colorama import Fore, Style

# colorama.init()

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

#   Const
DESKTOP_DIR = os.path.expanduser('~') + r'\Desktop'
file_path = DESKTOP_DIR + r'\text.txt'
way = ''


def error_out(s):  # Вывод красного текста
    print(RED + s + RESET, sep='')


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s + RESET, sep='')


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s + RESET, sep='')


def encodings():
    print(f'\n\tsys.getdefaultencoding(): {sys.getdefaultencoding()}')
    print(f'\tlocale.getpreferredencoding(): {locale.getpreferredencoding()}')
    print(f'\tsys.stdout.encoding: {sys.stdout.encoding}')
    print(f'\tsys.getfilesystemencoding(): {sys.getfilesystemencoding()}')
    print(f'\tsys.gettrace(): {sys.gettrace()}')
    print(f'\tsys.getswitchinterval(): {sys.getswitchinterval()}')
    print(f'\tsys.getprofile(): {sys.getprofile()}')
    print(f'\tsys.getwindowsversion(): {sys.getwindowsversion()}\n')


def file_open():  # Проверка готовности файла
    while True:
        yellow_out("Введите полный путь до файла, кодировку которого надо узнать.")
        print("Введите '-' если хотите выйти из программы")
        ans = input()

        if ans == "-":
            return 0

        else:
            try:
                with open(file=ans, mode='r') as _:
                    done_out('\nВсё ок! Файл открыт!\n')
                    global way
                    way = ans
                    return 1

            except FileNotFoundError:  # Ошибка
                error_out("\nFileNotFoundError: У вас нет файла по данному пути!\n"
                          "P.S. Надо ввести путь с именем файла.\n")


def main():
    # file_path = r'some'
    with open(way, "r") as file:
        encode = file.encoding
        print('*' * 20)
        print(f"File: {file}\n"
              f"type(file): {type(file)}\n"
              f"file.name: {file.name}\n"
              f"file.mode: {file.mode}\n"
              f"file.encoding: {file.encoding}\n"
              f"file.buffer: {file.buffer}\n"
              f"file.errors: {file.errors}\n"
              f"file.line_buffering: {file.line_buffering}\n"
              f"file.newlines: {file.newlines}")

    print('*' * 20)
    print(f"encoding: {encode}\ntype(encoding): {type(encode)}")
    print('*' * 20)

    with open(way, "r", encoding=encode) as f:
        s = f.read()
        print('In file:\n', s, sep='')


if __name__ == '__main__':
    # main()
    if file_open():
        main()
    encodings()
