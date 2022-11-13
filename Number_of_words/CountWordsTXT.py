import time
import os
import pyautogui as pg
import random

# Const
HOME_DIR = os.path.expanduser('~') + r'\Desktop'


# print("Путь к рабочему столу: " + HOME_DIR + "\n")

def clear():  # Очистка консоли
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def styles_format():  # Выводы текста возможные
    for style in range(10):
        for c_text in range(30, 38):
            for c_bg in range(40, 48):
                code = f"033[{style};{c_text};{c_bg}m"
                print(f"\033[{style};{c_text};{c_bg}m Some Text; \033[0m Code: \{code}")


def check_set():  # Возврат длины set() == количество различных символов(кодов)
    file = open(file=HOME_DIR + r'\text.txt', mode='r', encoding='utf-8')
    lines = file.read()
    count_char = set(lines)
    # print(count_char, len(count_char))
    file.close()
    return len(count_char)


def check_ord(lines):  # Проверка кода символа
    for i in lines:
        print(i)
        s = input("Узнать код?(+/-): ")
        if s == "+":
            for char in i:
                print(ord(char), end=" ")


def check_symbol():  # Проверка символов в файле
    file = open(file=HOME_DIR + r'\text.txt', mode='r', encoding='utf-8')
    for line in file:
        line = line.lower()
        lines = line.split(' ')
        check_ord(lines)
        print(lines)

    file.close()


def exi_t():  # Выход из программы
    seconds = [0.03, 0.04, 0.05, 0.06]
    time.sleep(1.5)
    s = "\nСпасибо за использование нашей программы.\nВсего хорошего!\n;)\n"
    for i in s:
        print(i, end="")
        time.sleep(random.choice(seconds))
    time.sleep(3)
    exit()


def algorithm():  # Основной алгоритм
    ascii_punctuation = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                         46, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94,
                         95, 96, 123, 124, 125, 126, 171, 187, 8212]  # Знаки препинания
    dict_words = {}  # Словарь dict()
    count_words = 0
    count_digits = 0
    count_char = check_set()
    file = open(file=HOME_DIR + r'\text.txt', mode='r', encoding='utf-8')

    for line in file:

        line = line.lower()
        for char in line:
            if ord(char) in ascii_punctuation:
                line = line.replace(char, ' ')

        lines = line.split(' ')
        for item in lines:
            if item:  # Не пустая строка
                item = item.strip()
                if "\n" in item and len(item) != 1:  # Если без пробела началась новая строка
                    item = item[:-1]
                    try:
                        dict_words["\n"] += 1
                    except KeyError:
                        dict_words["\n"] = 1
                try:
                    dict_words[item] += 1
                except KeyError:
                    dict_words[item] = 1
                finally:
                    if item.isdigit():
                        count_digits += 1
                    elif item != "\n":
                        count_words += 1
    file.close()

    print("Количество различных символов в файле: ", count_char)
    print("Количество слов в тексте: ", count_words)
    print("Количество чисел в тексте: ", count_digits)
    for item_keys in sorted(dict_words.keys()):
        if item_keys == "\n":
            print("Абзацев:", dict_words[item_keys], "\n")
        else:
            print(item_keys.title(), ": ", dict_words[item_keys])

    with open(file='Number_of_words.txt', mode='w', encoding='utf-8') as file_2:  # a
        n = "\n"
        file_2.write(f"Количество различных символов в файле: {count_char}\n")
        file_2.write(f"Количество слов в тексте: {count_words}\n")
        file_2.write(f'Количество чисел в тексте: {count_digits}\n')
        if "\n" in dict_words.keys():
            file_2.write(f'Абзацев: {dict_words[n]}\n')
        file_2.write(f'\n')

        for item_keys in sorted(dict_words.keys()):
            if item_keys == "\n":
                pass
            else:
                file_2.write(f'{item_keys.title()}: {dict_words[item_keys]}\n')

    pg.alert(text=f"Количество слов в тексте: {count_words}\n", title='Итог работы программы', button='OK')
    return  # Прочитан весь файл


def file_open():  # Проверка готовности файла
    while True:
        print("Создайте на рабочем столе текстовый файл с нужным содержанием и именем: 'text.txt'")
        print("Введите '-' если хотите выйти из программы")
        print("Введите '+' если создали файл text.txt: ")
        s = input()

        if s == "-":
            return 0

        elif s == "+":
            try:
                with open(file=HOME_DIR + r'\text.txt', mode='r', encoding='utf-8') as _:
                    print('\nВсё ок! Файл открыт!\n')
                    return 1

            except FileNotFoundError:  # Ошибка
                print("\nУ вас НЕТ на рабочем столе файла с именем 'text.txt'!\n")

        else:
            print("\nВы ввели иной символ не подходящий для данной программы(\n")


def main():  # Старт программы
    hello = " \033[3;34mПрограмма по подсчёту слов текста из файла\033[0m "
    print("{:*^62}".format(hello), "\n")

    # check_symbol()
    # check_set()
    if file_open() == 1:
        algorithm()

    exi_t()


if __name__ == "__main__":
    main()
