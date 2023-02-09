# Add encoding file and color in file !

import random
import time
import os

from colorama import Fore, Style, init

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

# Const
# HOME_DIR = os.path.expanduser('~')
DESKTOP_DIR = os.path.expanduser('~') + r'\Desktop'
# DESKTOP_DIR = os.path.join(HOME_DIR, "Desktop")
chars = '+-/*!$#?=@<>1234567890'  # Все возможные символы и цифры


# print("Путь к рабочему столу: " + DESKTOP_DIR + "\n")

def error_out(text: str) -> None:
    """ Red text output """
    print(RED + text, sep='')


def done_out(text: str) -> None:
    """ Green text output """
    print(GREEN + text, sep='')


def yellow_out(text: str) -> None:
    """ Yellow text output """
    print(YELLOW + text, sep='')


def exi_t() -> None:
    """ Exiting the program """

    text = '\nСпасибо за использование нашего продукта!\nХорошего дня!\n'
    for sym in text:
        print(GREEN + sym, end='')
        time.sleep(random.choice([0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04]))
    input()
    exit()


def add_letters(shift: int) -> None:  # Добавление букв
    global chars  # Изменение переменной chars вне функции add_letters() тоже

    for i in range(26):
        chars += chr(i + shift)


def quest(mes: str) -> int:  # Ввод int
    while True:
        user_input = input(mes)

        if user_input.isdigit() and int(user_input) > 0:  # Проверка число ли и положительности
            break
        elif user_input == '000':
            exi_t()
        else:
            error_out('Надо ввести целое положительное ЧИСЛО!\nЕсли хотите выйти, то введите "000".\n')

    return int(user_input)


def out_password() -> None:  # Вывод паролей в консоль
    answer_pol = ['да', 'yes', 'yeah', '+', 'y']  # Возможные положительные ответы
    answer_neg = ['нет', 'no', 'not', 'none', '-', 'n']  # Возможные отрицательные ответы
    while True:
        s = input(YELLOW + 'Желаете их вывести в консоли?\nВведите Ваш ответ: ' + RESET)

        if s.lower() in answer_pol:
            f = open(file=DESKTOP_DIR + r'\passwords.txt', mode='r', encoding='cp1251')

            for i, line in enumerate(f):
                if i > 0:
                    print(line, end='')
            f.close()
            return

        elif s.lower() in answer_neg:
            return

        else:
            error_out("\nВы ввели иной ответ не предугаданный разработчиком(")
            print("Возможные положительные варианты ответов: \n", answer_pol)
            print("Возможные отрицательные варианты ответов: \n", answer_neg)


def generation(length: int) -> str:
    password = ""

    # Кол-во цифр, букв верхнего и нижнего регистра, и символов
    digit_count, upper_count, lower_count, sym_count = 0, 0, 0, 0
    for i in range(length):
        new_sym = random.choice(chars)

        if i == 0:
            while new_sym not in chars[22::]:  # Проверка того, что первый символ в пароле не число или знак
                new_sym = random.choice(chars)

        # Счет цифр и букв верхнего и нижнего регистра
        if new_sym.isdigit():
            digit_count += 1
        elif new_sym.isupper():
            upper_count += 1
        elif new_sym.islower():
            lower_count += 1
        else:
            sym_count += 1

        password += new_sym

    # Проверка надежности пароля
    if not (digit_count and upper_count and lower_count and sym_count):
        return generation(length)

    return password


def in_file(number: int, length: int) -> None:
    """ Ввод сгенерированных паролей в файл """

    file = open(file=DESKTOP_DIR + r'\passwords.txt', mode='w', encoding='utf-8')  # Открытие файла на рабочем столе
    file.write('Ваши пароли: \n')

    for x in range(number):
        password = generation(length)  # Генерация паролей тут!
        file.write(f'\n{str(x + 1)} password: \n{password}\n')

    done_out('Пароли сгенерированы и сохранены в файле "passwords.txt" на Вашем рабочем столе.')
    file.close()  # Закрытие файла


def app() -> None:  # Основная программа
    global chars

    add_letters(65)  # Добавление в список shars заглавных латинских букв
    add_letters(97)  # Добавление в список shars строчных латинских букв

    number = quest('Введите кол-во паролей: ')
    while True:
        length = quest('Введите длину пароля: ')
        if length < 8:
            error_out("Для надежного пароля длина должна быть >8!")
        else:
            break

    in_file(number, length)  # Генерация паролей тут!
    out_password()
    exi_t()


if __name__ == '__main__':
    hello = YELLOW + " Программа по генерации случайных паролей " + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')
    app()  # Вызов работы программы
