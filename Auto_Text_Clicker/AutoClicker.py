import pyautogui as auto
import keyboard as key

# import mouse
auto.FAILSAFE = True


def listen_keyboard():  # Not use!!!
    text = '''
        CHOICE: 
            1) Some;
            2) Next;
            3) Exit;
          Esc -> for exit
    '''

    while True:
        print(text)
        k = key.read_key()
        if k == '1':
            print(111)
        elif k == '2':
            print(222)
        elif k == '3':
            print(333)
        elif k == 'esc':
            break


def main():
    start_key = input('Клавиша запуска: ')
    stop_key = input('Клавиша остановки: ')

    count_click = 0
    while True:
        if key.is_pressed(start_key):
            # auto.click()
            auto.click(clicks=10)  # , interval = 0.1
            # auto.doubleClick()
            # auto.tripleClick()
            count_click += 1  # * 10 clicks

        if key.is_pressed(stop_key):
            break

    print(f"Number of clicks = {count_click}")


if __name__ == "__main__":
    main()
