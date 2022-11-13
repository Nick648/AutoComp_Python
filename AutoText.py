# Add encoding file and colorama !
import keyboard
import random
import time
import os

from colorama import Fore, Style

# colorama.init()

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

# Const os
# HOME_DIR = os.path.expanduser('~')
DESKTOP_DIR = os.path.expanduser('~') + r'\Desktop'


def error_out(s):  # Вывод красного текста
    print(RED + s + RESET, sep='')


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s + RESET, sep='')


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s + RESET, sep='')


# print("Путь к рабочему столу: " + DESKTOP_DIR + "\n")

def file_open():  # Проверка готовности файла
    while True:
        print("Создайте на рабочем столе текстовый файл с нужным содержанием и именем: 'text.txt'")
        print("Введите '-' если хотите выйти из программы")
        print("Введите '+' если изменили путь и создали файл text.txt: ")
        s = input()

        if s == "-":
            return 0

        elif s == "+":
            try:
                with open(file=DESKTOP_DIR + r'\text.txt', mode='r') as file:
                    done_out('\nВсё ок! Файл открыт!\n')

                    global encode
                    try:
                        encode = file.encoding
                        # print(f"Encode: {encode}")
                    except:
                        error_out("Кодировка файла не распознана! По умолчанию будет: 'utf-8'")
                        encode = 'utf-8'

                    return 1

            except FileNotFoundError:  # Ошибка
                error_out("\nFileNotFoundError: У вас нет на рабочем столе файла с именем 'text.txt'!\n")

        else:
            error_out("\nВы ввели иной символ не подходящий для данной программы(")


def exec_app():  # Основной алгоритм
    description = "Для написания текста зажмите клавишу 'Ctrl' \nДля выхода из программы нажмите 'esc'"
    description += "\nНажатие клавиши 'esc' ОЧЕНЬ ВАЖНО для корректного завершения программы"
    description += "\nP.S. Программа как и человек может ошибаться! " \
                   "Советуем посмотреть правильность набранного текста в итоге"

    f = open(file=DESKTOP_DIR + r'\text.txt', mode='r', encoding=encode)  # encoding='windows-1251'

    for line in f:
        i = 0
        while True:
            if keyboard.is_pressed('Ctrl'):
                # time.sleep(0.001)
                k = random.randint(20, 150)  # Задание определенного интервала для печатания символов
                k = k / 1000

                if len(line) == i:  # Если строка подошла к концу
                    break

                keyboard.write(line[i], delay=k)
                i += 1

            if keyboard.is_pressed('esc'):
                f.close()
                return 0  # Прочитан не весь файл

    f.close()
    return 1  # Прочитан весь файл


def main():  # Старт программы
    hello = " \033[3;34m Имитация набора текста \033[0m "
    print("{:*^62}".format(hello), "\n")
    yellow_out("Программа по автоматическому выводу текста из файла")

    if file_open():
        if exec_app() == 1:
            keyboard.write("\nГотово!\n", delay=0.1)
            done_out("\nВсе что было в файле выписано!")

    # print("Ok, для завершения работы нажмите еще раз 'esc'")
    # keyboard.wait('esc')

    done_out("\nВсего хорошего!")

    time.sleep(3)
    # keyboard.send("Ctrl+Shift+esc")  # Диспетчер задач - ХЗ


if __name__ == '__main__':
    main()
