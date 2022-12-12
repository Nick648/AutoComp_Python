from tkinter import *
from tkinter import filedialog
from PIL import Image
import os


def is_valid(newval):
    print(newval)
    if not os.path.isfile(newval):
        errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    else:
        errmsg.set("")


def convert():  # Add text box into down!
    path_to_file_png = path_to_png.get()
    if os.path.isfile(path_to_file_png):
        img = Image.open(path_to_png.get())
        img.save('output.ico')
    else:
        print(f'{path_to_file_png} not exist!')


if __name__ == '__main__':
    root = Tk()
    root.title('Конвертер PNG в ICO')
    root.geometry('500x100')
    root.resizable(width=False, height=False)
    root['bg'] = 'black'

    # check = (root.register(is_valid), "%P")
    # errmsg = StringVar()

    path_to_png = Entry(root, width=50, font='Arial 10 bold')  # , validate="key", validatecommand=check
    path_to_png.pack(pady=10)

    btn_convert = Button(root, text='Конвертировать в ICO', font='Arial 15 bold', command=convert)
    btn_convert.pack(pady=10)

    root.mainloop()
