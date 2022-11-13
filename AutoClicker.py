import pyautogui as auto
import keyboard as key
import mouse


def main():
    start_key = input('Клавиша запуска: ')
    stop_key = input('Клавиша остановки: ')

    i = 0

    while True:
        if key.is_pressed(start_key):
            # auto.click()
            auto.click(clicks=10)  # , interval = 0.1
            # auto.doubleClick()
            # auto.tripleClick()
            i += 1

        if key.is_pressed(stop_key):
            break

    print(i)


if __name__ == "__main__":
    main()
