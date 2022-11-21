import pyautogui as pg
import tkinter as tk
import keyboard
import time
from math import sqrt
from colorama import Fore, Style, init

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL

WIDTH, HEIGHT = pg.size()  # Get the size of the primary monitor.


# Узнать координаты непрерывно
def find_pos_infinity():
    start_key = input('Клавиша запуска: ')
    stop_key = input('Клавиша остановки: ')

    while True:
        if keyboard.is_pressed(start_key):
            time.sleep(0.3)
            print(pg.position())

        if keyboard.is_pressed(stop_key):
            print('thanks')
            break


# pg.alert(text = 'To use, press: "Ctrl"', title = 'Position of mouse', button = 'OK')

def main():
    print(f"SIZE WINDOW(x,y): {WIDTH}x{HEIGHT}\n")

    root = tk.Tk()
    root.resizable(False, False)
    root.attributes("-topmost", True)  # Поверх других окон!!!

    root.title('Location mouse')
    greeting = f"Size window: {WIDTH}x{HEIGHT}\n" + "Press: 'Ctrl' to start\n" + "Press: 'Esc' to stop"
    label = tk.Label(root, font=('Ubuntu', 30), fg='magenta', text=greeting)
    label.pack()
    mouse_x0 = -1
    mouse_y0 = -1
    while True:
        if keyboard.is_pressed('Esc'):
            bye = "Thank you for using the program!"
            label.config(text=bye, fg='green')
            try:
                root.update()
            except Exception as ex:
                print(RED + f'Error: {ex}')
            break

        if keyboard.is_pressed('Ctrl'):
            mouse_x, mouse_y = pg.position()  # Get the X and Y position of the mouse.
            if mouse_x0 == -1 and mouse_y0 == -1:
                s = f"Size window: {WIDTH}x{HEIGHT}\n"
                s += f"Location mouse: {mouse_x} {mouse_y}"
                print(s, "\n", "-" * 20)
                mouse_x0 = mouse_x
                mouse_y0 = mouse_y
                label.config(text=s, fg='black')
            else:
                distance_x = mouse_x - mouse_x0
                distance_y = mouse_y - mouse_y0
                distance_diagonal = sqrt(distance_x ** 2 + distance_y ** 2)
                s = f"Size window: {WIDTH}x{HEIGHT}\n"
                s += f"Location mouse: {mouse_x} {mouse_y}\n"
                s += f"Recently location mouse: {mouse_x0} {mouse_y0}\n"
                s += f"Moving(x,y): {distance_x} {distance_y}"
                if distance_diagonal != 0:
                    if distance_diagonal == int(distance_diagonal):
                        distance_diagonal = int(distance_diagonal)
                    else:
                        distance_diagonal = "{:.5f}".format(distance_diagonal)
                    s += f"\nDistance(diagonal): {distance_diagonal}"
                print(s[s.find('\n') + 1:], "\n", "-" * 20)
                mouse_x0 = mouse_x
                mouse_y0 = mouse_y
                label.config(text=s, fg='black')

            time.sleep(0.3)

        try:
            root.update()
        except Exception as ex:  # TclError
            print(RED + f'Error: {ex} \n\tName: {type(ex).__name__}; Type: {type(ex)}')
            break

    # root.mainloop()
    print("\n------->", GREEN + "Done")
    time.sleep(2)


if __name__ == '__main__':
    hello = YELLOW + " A program for finding the mouse position on the screen "
    print("\n", "{:*^75}".format(hello), "\n")
    main()
    # find_pos_infinity()
