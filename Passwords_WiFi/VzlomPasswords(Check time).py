import time
import keyboard as key


def decoding(s):  # Расшифровка
    for i in range(1301):
        if s == chr(i):
            return chr(i)


def main():  # Основной алгоритм
    while True:
        s = input("Введите пароль: ")
        if key.is_pressed('Esc'):
            return
        s1 = ""
        tic = time.perf_counter()
        for i in range(len(s)):
            s1 += decoding(s[i])
        toc = time.perf_counter()
        print("Ваш пароль:", s1)
        print("Времени заняло:", toc - tic, "seconds\n")


if __name__ == '__main__':
    print("Взлом пароля, проверка времени.\nДля выхода нажмите 'Esc'.")
    main()  # Запуск основного алгоритма
