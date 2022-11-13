import time  # Модуль time


def exi_t():  # Выход из программы
    a = 'Спасибо за использование нашего продукта!\nХорошего дня!'
    for i in a:
        print(i, end='')
        time.sleep(0.027)  # Приостановить выполнение программы
    input()
    exit()


def qu(s):  # Ввод времени
    while True:
        t = input(s)
        print()
        if t.isdigit():
            if int(t) >= 0:
                return int(t)
            else:
                print("Число должно быть положительное!\n")
        else:
            print("Вы должны ввести положительное ЧИСЛО!\n")


def qu_1():  # Выбор варианта событий
    a = ["1", "2"]
    while True:
        t = input('Вариант: ')
        print()
        if t not in a:
            print('Такого варианта нет! Пожалуйста выберите из предложенного.\n')
        else:
            return int(t)


def schet(t, i):  # Расчет нового времени при воспроизведении
    a = [0, 0, 0]
    t1 = t / i
    a[2] = int(t1 % 60)
    t1 //= 60
    a[1] = int(t1 % 60)
    t1 //= 60
    a[0] = int(t1 % 60)
    return a


def outPut(t):  # Вывод работы основной
    a = [0.25, 0.5, 0.75, 1.25, 1.5, 1.75, 2, 2.5, 3]
    print("\nВидео длится при скорости воспроизведения: ", end="")
    for i in a:
        if i == 1.25:
            print()
        print("\n * " + str(i) + "x) ", end="")
        t1_out = schet(t, i)
        if t1_out[0] != 0:
            print(t1_out[0], "часов", end=" ")
        if t1_out[1] != 0:
            print(t1_out[1], "минут", end=" ")
        if t1_out[2] != 0:
            print(t1_out[2], "секунд", end=" ")
    return


def algorithm():  # Основной алгоритм
    h = qu("Введите сколько часов идёт исходное видео: ")
    m = qu("Введите сколько минут идёт исходное видео: ")
    s = qu("Введите сколько секунд идёт исходное видео: ")
    t = (h * 60 * 60) + (m * 60) + s
    print("Исходное видео(скорость воспроизведения = 1) длится: ", end="")
    if h != 0:
        print(h, "часов", end=" ")
    if m != 0:
        print(m, "минут", end=" ")
    if s != 0:
        print(s, "секунд", end=" ")
    if h == 0 and m == 0 and s == 0:
        print("0 секунд")
        print("Соответственно всегда будет длиться 0 секунд")
        exi_t()
    outPut(t)
    return


def main():  # Старт программы
    print("Длительность воспроизведения от скорости воспроизведения.")
    print("Выберите вариант работы программы: ")
    while True:
        print("1) Расчёт времени\n2) Выход")
        t = qu_1()
        if t == 1:
            algorithm()
            print("\n")
        elif t == 2:
            exi_t()


main()
