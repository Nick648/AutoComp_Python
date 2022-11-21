import time
import os
import pyperclip
from PIL import ImageGrab, Image
import datetime
import keyboard
from colorama import Fore, Style
import pyautogui
from fpdf import FPDF
from tkinter import Tk

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


# For further development
def display_resize_info(monitor_width, monitor_height, width, height):
    print(f'Size screen: {monitor_width}x{monitor_height}')
    print(f'The original image size is wide x high: {width} x {height}')
    wc, ws = monitor_width // width, monitor_width / width
    hc, hs = monitor_height // height, monitor_height / height
    k_increase = min(monitor_width / width, monitor_height / height)
    k_increase_int = min(monitor_width // width, monitor_height // height)
    print(f'{monitor_width}/{width} -> {wc} : {ws} \n'
          f'{monitor_height}/{height} -> {hc} : {hs}\n')
    print(f'{wc}: {monitor_width}x{monitor_height} -> {wc * width}x{wc * height}\n'
          f'{ws}: {monitor_width}x{monitor_height} -> {ws * width}x{ws * height}\n'
          f'{hc}: {monitor_width}x{monitor_height} -> {hc * width}x{hc * height}\n'
          f'{hs}: {monitor_width}x{monitor_height} -> {hs * width}x{hs * height}\n')
    print(f'{k_increase=}: {width * k_increase}x{height * k_increase}')
    print(f'{k_increase_int=}: {width * k_increase_int}x{height * k_increase_int}')


def fpdf_create_file():  # Create pdf file using 'fpdf' module
    root = Tk()
    monitor_height = root.winfo_screenheight()
    monitor_width = root.winfo_screenwidth()

    # width, height = 1600, 900  # Screen size
    pdf = FPDF(unit='pt', format=(monitor_width, monitor_height))

    for img_name in os.listdir(WAY_DIR):
        if img_name[img_name.rfind('.'):] != '.png':  # If it's different file (not .png)
            continue
        img_path = os.path.join(WAY_DIR, img_name)
        pdf.add_page()
        image_item = Image.open(img_path)
        width, height = image_item.size

        # display_resize_info(monitor_width, monitor_height, width, height)
        k_increase = min(monitor_width // width, monitor_height // height)
        if k_increase > 1:
            if not os.path.exists(os.path.join(WAY_DIR, 'Resized Images')):  # Creating a folder for Resized Images
                os.mkdir(os.path.join(WAY_DIR, 'Resized Images'))
            # print(f'Original: {width}x{height}')
            resized_image = image_item.resize((width * k_increase, height * k_increase))
            resized_img_path = os.path.join(WAY_DIR, 'Resized Images', "Resized " + img_name)
            resized_image.save(resized_img_path)
            width, height = resized_image.size
            # print(f'  ->  Resized: {width}x{height}')

        pos_xo, pos_y0 = monitor_width / 2 - width / 2, monitor_height / 2 - height / 2
        pdf.image(img_path, pos_xo, pos_y0, width, height)

    filename_pdf = WAY_DIR[WAY_DIR.rfind('\\') + 1:] + ' (1).pdf'
    filename_pdf = os.path.join(WAY_DIR, 'PDF files', filename_pdf)
    pdf.output(filename_pdf)
    print(f'Save as: {filename_pdf}\t{GREEN + "Done!" + RESET}')


def image_create_file():  # Create pdf file using 'PIL' module
    images_list = list()
    for img_name in os.listdir(WAY_DIR):
        if img_name[img_name.rfind('.'):] != '.png':  # If it's different file (not .png)
            continue
        img_path = os.path.join(WAY_DIR, img_name)
        image_item = Image.open(img_path)
        # image_item = image_item.convert('RGB')
        images_list.append(image_item)
    # print(f'{images_list=}')

    filename_pdf = WAY_DIR[WAY_DIR.rfind('\\') + 1:] + ' (2).pdf'
    filename_pdf = os.path.join(WAY_DIR, 'PDF files', filename_pdf)
    images_list[0].save(filename_pdf, save_all=True, append_images=images_list)  # , quality=100
    print(f'Save as: {filename_pdf}\t{GREEN + "Done!" + RESET}')


# The issue of creating a pdf report
def create_pdf_file():
    y_ans = ['y', 'ye', 'yes', 'yeah']
    n_ans = ['n', 'no', 'non', 'none']
    while True:
        op = input(GREEN_1 + 'Add images to pdf file? (Y/N) \n>>> ' + RESET).strip().lower()
        if op in n_ans:
            return
        elif op in y_ans:
            if not os.path.exists(os.path.join(WAY_DIR, 'PDF files')):  # Creating a folder for files.pdf
                os.mkdir(os.path.join(WAY_DIR, 'PDF files'))
            fpdf_create_file()
            image_create_file()
            return
        else:
            print(RED + 'Enter the appropriate answer: (Y/N)\n' + RESET)


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
            print(YELLOW + "=" * 40 + RESET)
        if keyboard.is_pressed('Esc'):
            break

        time.sleep(0.3)  # The problem with ImageGrab.grabclipboard() if you remove sleep

    if count > 0:
        create_pdf_file()
    print(MAGENTA + f'\n\tTotal screenshots: {count}')
    print(f'\tThe images were saved in a folder: {WAY_DIR}')
    print(f'\tList of screenshot names: {[i for i in (os.listdir(WAY_DIR)) if i[-4:] == ".png"]}' + RESET)


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
