import time
import os
import pyperclip
from PIL import ImageGrab, Image
import datetime
import keyboard
from colorama import Fore, Style
import pyautogui

# colorama.init()
# Const module colorama
GREEN = Fore.LIGHTGREEN_EX
GREEN_1 = Fore.GREEN
RED = Fore.LIGHTRED_EX
YELLOW = Fore.LIGHTYELLOW_EX
WHITE = Fore.LIGHTWHITE_EX
MAGENTA = Fore.LIGHTMAGENTA_EX
CYAN = Fore.LIGHTCYAN_EX
RESET = Style.RESET_ALL

# Consts for time and date
today = datetime.datetime.today()
date_y, date_m, date_d = today.year, today.month, today.day
# time_h, time_m, time_s = today.hour, today.minute, today.second

# Name of directory
CUR_DIR_FILE = os.path.abspath(__file__)  # Full path to the file, with name file.py
CUR_DIR = os.path.dirname(os.path.abspath(__file__))  # Without name file.py
NAME_DIR = f'Screenshots {date_d}_{date_m}_{date_y}'
WAY_DIR = os.path.join(CUR_DIR, NAME_DIR)


# Creating a folder
def create_dir():
    global WAY_DIR, NAME_DIR

    if not os.path.exists(WAY_DIR):  # Creating a folder for images
        os.mkdir(WAY_DIR)

    # If the folder is created, an additional one will be created with the version specified
    else:
        version = 1
        while os.path.exists(WAY_DIR):
            NAME_DIR = f'Screenshots {date_d}_{date_m}_{date_y} version=={version}'
            WAY_DIR = os.path.join(CUR_DIR, NAME_DIR)
            version += 1
        os.mkdir(WAY_DIR)


def add_pdf_file():
    y_ans = ['y', 'ye', 'yes', 'yeah']
    n_ans = ['n', 'no', 'non', 'none']
    while True:
        op = input(GREEN_1 + 'Add images to pdf file? (Y/N) \n>>> ' + RESET).strip().lower()
        if op in n_ans:
            return
        elif op in y_ans:
            images_list = list()
            for img_name in os.listdir(WAY_DIR):
                img_path = os.path.join(WAY_DIR, img_name)
                image_item = Image.open(img_path)
                # print(f'{image_item=}')
                # image_item = image_item.convert('RGB')
                images_list.append(image_item)
            # print(f'{images_list=}')

            filename_pdf = WAY_DIR[WAY_DIR.rfind('\\') + 1:] + '.pdf'
            filename_pdf = os.path.join(WAY_DIR, filename_pdf)
            images_list[0].save(filename_pdf, save_all=True, append_images=images_list)  # , quality=100
            print(f'\nSave as: {filename_pdf}\t{GREEN + "Done!" + RESET}')
            return
        else:
            print(RED + 'Enter the appropriate answer: (Y/N)\n' + RESET)


# Reading the clipboard
def reading_clipboard():
    print(YELLOW + "=" * 30 + RESET)
    pyperclip.copy('Easter Egg')  # If there is already a screen at startup, do not take it
    old_copy = None
    count = 0
    while True:
        try:
            copy_im = ImageGrab.grabclipboard()
        except Exception as ex:  # OSError: failed to open clipboard
            copy_im = None
            print(RED + f'Reading error! Check that the screenshot is saved correctly' + RESET)
            pyautogui.alert(text='Ошибка чтения!\nПроверьте корректное сохранение скриншота',
                            title='Предупреждение', button='Ok')

        if old_copy != copy_im and copy_im is not None:
            count += 1
            old_copy = copy_im
            time_now = datetime.datetime.today()
            time_h, time_m, time_s = time_now.hour, time_now.minute, time_now.second
            name_screen = os.path.join(WAY_DIR, f'Screen {count}  ({time_h}-{time_m}-{time_s}).png')
            print(copy_im, type(copy_im))
            print(f'\t{GREEN + f"Copy {count} Done!" + RESET} Save as: {name_screen}')
            copy_im.save(name_screen, 'PNG')
            print(YELLOW + "=" * 30 + RESET)
        if keyboard.is_pressed('Esc'):
            break

        time.sleep(0.3)  # The problem with ImageGrab.grabclipboard() if you remove sleep

    if count > 0:
        add_pdf_file()
    print(MAGENTA + f'\n\tTotal screenshots: {count}')
    print(f'\tThe images were saved in a folder: {WAY_DIR}')
    print(f'\tList of screenshot names: {os.listdir(WAY_DIR)}' + RESET)


def main():
    create_dir()
    reading_clipboard()


if __name__ == '__main__':
    greeting = '''
        A program for saving screenshots taken in PNG format. 
        The file folder will appear in the folder next to the program.
        Click for:
          Esc - for early exit;
        Enjoy using it!
        '''
    print(YELLOW + greeting + RESET)
    main()
