import time
import os
from PIL import ImageGrab
import requests

from colorama import Fore, Style

# colorama.init()
# Const module colorama
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def main():
    print(YELLOW + "=" * 30 + RESET)
    old_copy = None
    while True:
        copy_im = ImageGrab.grabclipboard()
        if old_copy != copy_im and copy_im is not None:
            print(copy_im, type(copy_im), "Copy Done!")
            old_copy = copy_im
            copy_im.save('screen_pic_del.png', 'PNG')

            test_files = {"test_file_1": open('screen_pic_del.png', "rb")}
            r = requests.post('https://img2txt.com/ru', files=test_files)
            test_files["test_file_1"].close()

            print(r, r.text, sep='\n')
            print(YELLOW + "=" * 30 + RESET)
            time.sleep(1)
            os.remove('screen_pic_del.png')

        time.sleep(1)


if __name__ == '__main__':
    main()
