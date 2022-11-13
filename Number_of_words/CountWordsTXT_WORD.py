import time
from docx import Document
# import docx
import os


def exi_t():  # Выход из программы
    a = 'Спасибо за использование нашего продукта!\nХорошего дня!'
    for i in a:
        print(i, end='')
        time.sleep(0.03)  # Приостановить выполнение программы
    input()
    exit()


def fileOpen(s):  # Проверка готовности файла
    while True:

        if s == "-":
            return 0

        elif s == "+":
            try:
                with open(r"C:\Users\Dima\Desktop\text.txt", 'r', encoding='utf-8') as f:
                    print('\nВсё ок! Файл открыт!\n')
                    return 1

            except:  # Ошибка
                print("\nУ вас нет на рабочем столе файла с именем 'text.txt'!")
                print("Создайте на рабочем столе текстовый файл с нужным содержанием и именем: 'text.txt'")
                print("Введите '+' если изменили путь и создали файл text.txt: ")
                print("Введите '-' если хотите выйти из программы\n")

        else:
            print("\nВы ввели иной символ не подходящий для данной программы(")
            print("Введите '+' если изменили путь и создали файл text.txt: ")
            print("Введите '-' если хотите выйти из программы\n")

        s = input()


def algoritm_Txt():  # Основной алгоритм
    asci = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94, 95, 96,
            123, 124, 125, 126, 8212]  # Знаки препинания
    d = {}  # Словарь
    k = 0
    f = open(r"C:\Users\Dima\Desktop\text.txt", 'r', encoding='utf-8')

    for line in f:

        line = line.lower()
        for i in line:
            if ord(i) in asci:
                line = line.replace(i, ' ')

        line = line.split(' ')
        for i in line:
            if i:  # Не пустая строка
                k += 1
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

    print("Количество слов в тексте: ", k - d["\n"])
    for i in sorted(d.keys()):
        if i == "\n":
            print("Абзацев:", d[i], "\n")
        else:
            print(i.title(), ": ", d[i])

    f.close()
    return d  # Прочитан весь файл


def algoritm_Word():  # Основной алгоритм
    asci = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94, 95, 96,
            123, 124, 125, 126, 8212]  # Знаки препинания
    d = {}  # Словарь
    k = 0
    doc = docx.Document(r"C:\Users\Dima\Desktop\1.docx")
    all_paras = doc.paragraphs

    for para in all_paras:
        line = para.text.lower()
        for i in line:
            if ord(i) in asci:
                line = line.replace(i, ' ')

        line = line.split(' ')
        for i in line:
            if i:  # Не пустая строка
                k += 1
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

    print("Количество слов в тексте: ", k)
    print("Абзацев:", len(all_paras), "\n")
    for i in sorted(d.keys()):
        print(i.title(), ": ", d[i])
    return d


def qu(naz, naz_k):  # Выбор варианта событий
    a = []
    for i in range(len(naz_k)):
        a.append(str(i + 1))
    while True:
        print(naz)
        for i in range(len(naz_k)):
            print(naz_k[i])
        print()
        t = input('Вариант: ')
        print()
        if t not in a:
            print(
                'Такого варианта нет! Пожалуйста выберите из предложенного.\nМы работаем над разнообразием функций.\n')
        else:
            return int(t)


def main():  # Старт программы
    print("Программа по подсчёету слов текста из файла")
    naz = "Выберите откуда будет считывать текст(это важно для правильной работы программы!): "
    naz_k = ["1) С word файла(.docx)", "2) С текстового документа(.txt)", "3) Выход"]
    t = qu(naz, naz_k)
    if t == 1:
        print("Создайте на рабочем столе word файл с нужным содержанием и именем: 'text.docx'")
        print("!Для работы ОБЯЗАТЕЛЬНО измените путь до Вашего рабочего стола!")
        print("\nВведите '+' если изменили путь и создали файл text.docx: ")
        s = input()
        if fileOpen(s) == 1:
            d = algoritm_Word()
    elif t == 2:
        print("Создайте на рабочем столе текстовый файл с нужным содержанием и именем: 'text.txt'")
        print("!Для работы ОБЯЗАТЕЛЬНО измените путь до Вашего рабочего стола!")
        print("\nВведите '+' если изменили путь и создали файл text.txt: ")
        if fileOpen(s) == 1:
            d = algoritm_Txt()
    elif t == 3:
        exi_t()
    naz = "Выберите куда будем записывать результат программы: "
    naz_k = ["1) В word файл(.docx)", "2) В текстовый документ(.txt)", "3) В оба", "4) Выход"]
    if t == 1:
        pass
    elif t == 2:
        pass
    elif t == 3:
        pass
    elif t == 4:
        exi_t()
    t = qu(naz, naz_k)
    exi_t()


main()
