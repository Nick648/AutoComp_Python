# Add encoding file and color in file !

import random  # Добавление модуля random
import time  # Добавление модуля time
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
chars = '+-/*!$#?=@<>1234567890'  # Все возможные и цифры


# print("Путь к рабочему столу: " + DESKTOP_DIR + "\n")

def error_out(s):  # Вывод красного текста
    print(RED + s, sep='')


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s, sep='')


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s, sep='')


def exi_t():  # Выход из программы
    a = '\nСпасибо за использование нашего продукта!\nХорошего дня!\n'
    for i in a:
        print(GREEN + i, end='')
        time.sleep(random.choice([0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04]))  # Приостановить выполнение программы
    input()
    exit()


def add_letters(k):  # Добавление букв
    global chars  # Изменение переменной chars вне функции add_letters() тоже

    for i in range(26):
        chars += chr(i + k)


def quest(i):  # Ввод
    while True:
        q = input(i)

        if q.isdigit() and int(q) > 0:  # Проверка число ли и положительности
            break

        elif q == '000':
            exi_t()

        elif not (q.isdigit()) or int(q) <= 0:
            error_out('Надо ввести целое положительное ЧИСЛО!\nЕсли хотите выйти, то введите "000".\n')

    return int(q)


def out_password():  # Вывод паролей в консоль
    answer_pol = ['да', 'yes', 'yeah', '+', 'y']  # Возможные положительные ответы
    answer_neg = ['нет', 'no', 'not', 'none', '-', 'n']  # Возможные отрицательные ответы
    while True:
        s = input('\nВведите Ваш ответ: ')

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


def generation(length):
    password = ''
    dk, uk, lk = 0, 0, 0  # Кол-во цифр, букв верхнего и нижнего регистра
    for i in range(length):
        s = random.choice(chars)

        if i == 0 and s not in chars[22::]:  # Проверка того, что первый символ в пароле не число или знак
            while True:
                s = random.choice(chars)
                if s in chars[22::]:
                    break

        # Счет цифр и букв верхнего и нижнего регистра
        if s.isdigit():
            dk += 1
        if s.isupper():
            uk += 1
        if s.islower():
            lk += 1

        password += s

    # Проверка надежности пароля
    if dk <= 0 or uk <= 0 or lk <= 0:
        return generation(length)

    return password


def in_file(number, length):  # Ввод сгенерированных паролей в файл
    file = open(file=DESKTOP_DIR + r'\passwords.txt', mode='w', encoding='utf-8')  # Открытие файла на рабочем столе
    file.write('Ваши пароли: \n')

    for x in range(number):
        password = generation(length)  # Генерация паролей тут!
        k = str(x + 1) + ' password: '
        file.write(f'\n{str(x + 1)} password: \n{password}\n')
        # file.write('\n' + k)
        # file.write('\n' + password + '\n')

    done_out('Пароли сгенерированы и сохранены в файле "passwords.txt" на Вашем рабочем столе.')
    file.close()  # Закрытие файла


def app():  # Основная программа
    global chars

    add_letters(65)  # Добавление в список shars заглавных латинских букв
    add_letters(97)  # Добавление в список shars строчных латинских букв

    hello = YELLOW + " Программа по генерации случайных паролей " + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')

    number = quest('Введите кол-во паролей: ')
    while True:
        length = quest('Введите длину пароля: ')
        if length < 8:
            error_out("Для надежного пароля длина должна быть >8!")
        else:
            break

    in_file(number, length)  # Генерация паролей тут!
    yellow_out('Желаете их вывести в консоли?')
    out_password()
    exi_t()


if __name__ == '__main__':
    app()  # Вызов работы программы
