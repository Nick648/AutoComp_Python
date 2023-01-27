import time
import os
import keyboard
import pyperclip
from PIL import ImageGrab
import requests

from colorama import Fore, Style

add = '''
    Сделать прогу:
    1) Берет из буфера обмена картинку скрина текста;
    2) Закидывает ее на https://img2txt.com/ru;
    3) Получает оттуда текст расшифровки текста с скрина;
    4) Открывает блокнот записывает туда/кидает в буфер обмена;
'''

# colorama.init()
# Const module colorama
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

# Reading the clipboard
def reading_clipboard():
    print(YELLOW + "=" * 40 + RESET)
    pyperclip.copy('Easter Egg')  # If there is already a screen at startup, do not take it
    old_copy = None
    count = 0
    while True:
        try:
            copy_im = ImageGrab.grabclipboard()
        except Exception as ex:  # OSError: failed to open clipboard
            copy_im = None
            print(RED + f'Reading error! Check that the screenshot is saved correctly.  Error: {ex}' + RESET)

        if old_copy != copy_im and copy_im is not None:
            count += 1
            old_copy = copy_im
            # time_now = datetime.datetime.today()
            # time_h, time_m, time_s = time_now.hour, time_now.minute, time_now.second
            # name_screen = os.path.join(WAY_DIR, f'Screen {count}  ({time_h}-{time_m}-{time_s}).png')
            print(copy_im, type(copy_im))
            copy_im.save('screen_pic_del.png', 'PNG')
            test_files = {"test_file_1": open('screen_pic_del.png', "rb")}

            r = requests.post('https://img2txt.com/ru/file/upload-dropdown', files=test_files)
            print(r)
            print(r.content)
            print(r.json())

            test_files["test_file_1"].close()
            time.sleep(1)
            os.remove('screen_pic_del.png')
            # print(f'\t{GREEN + f"Copy {count} Done!" + RESET} Save as: {name_screen}')
            # copy_im.save(name_screen, 'PNG')
            print(YELLOW + "=" * 40 + RESET)
        if keyboard.is_pressed('Esc'):
            break

        time.sleep(1)  # The problem with ImageGrab.grabclipboard() if you remove sleep

def main():
    print(YELLOW + "=" * 30 + RESET)
    old_copy = None
    while True:
        copy_im = ImageGrab.grabclipboard()
        if old_copy != copy_im and copy_im is not None:
            print(copy_im, type(copy_im), "Copy Done!")
            old_copy = copy_im
            copy_im.save('screen_pic_del.png', 'PNG')

            print(YELLOW + "=" * 30 + RESET)
            time.sleep(1)
            os.remove('screen_pic_del.png')

        time.sleep(1)


def test():
    test_files = {"test_file_1": open('screen_pic_del.png', "rb")}
    r = requests.post('https://httpbin.org/post', files=test_files)
    print(r)
    print(r.content)
    print(r.json())
    test_files["test_file_1"].close()


if __name__ == '__main__':
    # test()
    # main()
    reading_clipboard()
