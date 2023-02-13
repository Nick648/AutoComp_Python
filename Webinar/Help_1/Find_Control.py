import pyautogui as pg
import time as tm
import keyboard
from datetime import datetime

from tkinter import *
from tkinter import filedialog

pg.FAILSAFE = True
pg.PAUSE = 1.5
WIDTH, HEIGHT = pg.size()  # Get the size of the primary monitor.

# Const paths files
IMG_CONTROL_WINDOW = r"data/Control_window.png"
IMG_CONTROL_BUTTON = r"data/Control_button.png"
# IMG_EXIT_WINDOW = r"data/Exit.jpg"
# IMG_EXIT_BUTTON = r"data/Exit_button.jpg"
REPORT_STR = ""
FILE_NAME = f"Report_webinar.txt"


def audio_play():
    print("Control found!")


def choose_img_file():
    pass


def tkinter_try_1():
    # Create object
    root = Tk()

    # Adjust size
    root.geometry("400x400")

    # Add image file
    bg = PhotoImage(file="Your_img.png")

    # Create Canvas
    canvas1 = Canvas(root, width=400,
                     height=400)

    canvas1.pack(fill="both", expand=True)

    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    # Add Text
    canvas1.create_text(200, 250, text="Welcome")

    # Create Buttons
    button1 = Button(root, text="Exit")
    button3 = Button(root, text="Start")
    button2 = Button(root, text="Reset")

    # Display Buttons
    button1_canvas = canvas1.create_window(100, 10,
                                           anchor="nw",
                                           window=button1)

    button2_canvas = canvas1.create_window(100, 40,
                                           anchor="nw",
                                           window=button2)

    button3_canvas = canvas1.create_window(100, 70, anchor="nw",
                                           window=button3)

    # Execute tkinter
    root.mainloop()


def tkinter_try_2():
    # Create object
    root = Tk()

    # Adjust size
    root.geometry("400x400")

    # Add image file
    bg = PhotoImage(file="Your_img.png")

    # Show image using label
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    # Add text
    label2 = Label(root, text="Welcome",
                   bg="#88cffa")

    label2.pack(pady=50)

    # Create Frame
    frame1 = Frame(root, bg="#88cffa")
    frame1.pack(pady=20)

    # Add buttons
    button1 = Button(frame1, text="Exit")
    button1.pack(pady=20)

    button2 = Button(frame1, text="Start")
    button2.pack(pady=20)

    button3 = Button(frame1, text="Reset")
    button3.pack(pady=20)

    # Execute tkinter
    root.mainloop()


def tkinter_window():
    start_window = Tk()
    win_width, win_height = 400, 600
    offset_width, offset_height = WIDTH // 2 - win_width // 2, HEIGHT // 2 - win_height // 2
    start_window.geometry(f"{win_width}x{win_height}+{offset_width}+{offset_height}")
    start_window.configure(background="pink")

    # C = Canvas(start_window, bg="blue", height=250, width=300)
    # filename = PhotoImage(file="data\maxresdefault.jpg")
    # background_label = Label(start_window, image=filename)
    # background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # C.pack()

    start_window.mainloop()

    # start_window.withdraw()
    # file_path = filedialog.askopenfilename()
    # print(file_path)


def report_to_file() -> None:
    with open(file=FILE_NAME, mode="w", encoding="utf-8") as file:
        file.write(REPORT_STR)


def display_report(mes: str) -> None:  # Add logger?
    global REPORT_STR
    today = datetime.today()
    date_y, date_m, date_d = today.year, today.month, today.day
    time_h, time_m, time_s = today.hour, today.minute, today.second
    report = f"{date_d}.{date_m}.{date_y} {time_h}:{time_m}:{time_s} -> {mes}"
    print(report)
    REPORT_STR += f"{report}\n"


def finder_control_window() -> int:
    display_report("Start finder_control_window")
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit finder_control_window")
            return 0

        find_control_window = pg.locateOnScreen(IMG_CONTROL_WINDOW, confidence=0.87)
        # find_control_add = pg.locateOnScreen('data/Control_add.jpg', confidence=0.9)
        tm.sleep(1)

        if find_control_window:
            display_report(f"{find_control_window=}")
            tm.sleep(0.5)
            pg.moveTo(find_control_window, duration=0.5)
            tm.sleep(0.5)
            find_control_button = pg.locateOnScreen(IMG_CONTROL_BUTTON, confidence=0.87, region=find_control_window)
            if find_control_button:
                display_report(f"{find_control_button=}")
                tm.sleep(0.5)
                pg.moveTo(find_control_button, duration=0.5)
                tm.sleep(0.5)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(0.5)
                display_report("finder_control_window done!\n")
                return 1
        tm.sleep(1)


def main() -> None:
    count_control = 0
    display_report("Start program")
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit main")
            break
        if finder_control_window():
            count_control += 1
        else:
            break
    display_report(f"Total count start control = {count_control}")
    display_report("Exit program")
    report_to_file()
    tm.sleep(2)


if __name__ == "__main__":
    print("The program for auto-marking on the webinar\n")
    tkinter_window()
    # main()
