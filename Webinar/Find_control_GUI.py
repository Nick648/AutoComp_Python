import pyautogui as pg
import time as tm
import os
from datetime import datetime
import shutil
import threading
from tkinter import *
from tkinter import filedialog, messagebox
import pyttsx3

pg.FAILSAFE = True
pg.PAUSE = 1.0
WIDTH, HEIGHT = pg.size()  # Get the size of the primary monitor.
WIN_WIDTH, WIN_HEIGHT = 400, 600

# Name of directories
DESKTOP_DIR = os.path.expanduser('~') + r'\Desktop'  # Full path to the desktop
NAME_DIR = f'Report Find_Control'
WAY_DIR = os.path.join(DESKTOP_DIR, NAME_DIR)

# Const paths files
IMG_CONTROL_WINDOW = os.path.join(WAY_DIR, r"Control_window.png")
IMG_CONTROL_BUTTON = os.path.join(WAY_DIR, r"Control_button.png")
IMG_EXIT_WINDOW = os.path.join(WAY_DIR, r"Exit_window.png")
IMG_EXIT_BUTTON = os.path.join(WAY_DIR, r"Exit_button.png")
NAME_REPORT_FILE = os.path.join(WAY_DIR, f"Report_control.txt")
NAME_BUGS_FILE = os.path.join(WAY_DIR, f"Report_bugs.txt")

lb_path_all: list[Label] = [None, None, None, None]
btn_all = []
lb_gif = None
gif_key = False
btn_start: Button = None
img_types = ['.jpg', '.jpeg', '.png']
REPORT_STR = ""
BUGS_STR = ""
TOTAL_COUNT_CONTROL = 0
FINDER_KEY = False
SLEEP_TIME_SEC = 0.2
DURATION_MOVE = 0.3
CONFIDENCE_VAL = 0.85


def create_dir() -> None:
    """ Creating a folder for files """
    if not os.path.exists(WAY_DIR):  # Creating a folder for files
        os.mkdir(WAY_DIR)
        display_report(f'Create {WAY_DIR}')


def long_line_wrap(label, text: str) -> None:
    # Принудительно обновляем интерфейс,
    # чтобы появилось окно и можно было получить фактическую ширину текста:
    root.update()
    if label.winfo_width() > root.winfo_width():
        # Вычисляем среднюю ширину символа
        average_char_width = label.winfo_width() / len(text)
        # Приблизительно рассчитываем количество символов, которое помещается в окне
        chars_per_line = int(root.winfo_width() / average_char_width)
        # В цикле уменьшаем это количество, пока текст не станет помещаться
        prev_width = label.winfo_width()
        while root.winfo_width() < label.winfo_width() <= prev_width:
            prev_width = label.winfo_width()
            wrapped_text = ""
            for pos, sym in enumerate(text):
                if pos == chars_per_line - 5:
                    wrapped_text += "\n    "
                wrapped_text += sym
            label['text'] = wrapped_text
            root.update()
            chars_per_line -= 1
    root.update()


def get_img_path() -> str:
    file_path = filedialog.askopenfilename()
    if file_path and not file_path[file_path.rfind('.'):].lower() in img_types:
        messagebox.showwarning(title="Предупреждение", message=f"Можно только выбрать изображение!\nТипы: {img_types}")
        return ""
    return file_path


def on_closing() -> None:
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        global FINDER_KEY
        FINDER_KEY = False
        display_report('Exiting the program')
        display_report(f"Total count start control = {TOTAL_COUNT_CONTROL}")
        root.destroy()
        tm.sleep(1.5)
        exit()


def set_sizes() -> None:
    root.resizable(False, False)
    offset_width, offset_height = WIDTH // 2 - WIN_WIDTH // 2, HEIGHT // 2 - WIN_HEIGHT // 2
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{offset_width}+{offset_height}")


def set_configure() -> None:
    root.title("Main window")
    # root.configure(background="white")
    # root.wm_attributes('-transparentcolor', root['bg'])  # Прозрачное приложение!
    # Add event for close window
    root.protocol("WM_DELETE_WINDOW", on_closing)


def display_gif():
    # global lb_gif
    # lb_gif = Label(root)
    size_gif = 18
    frames = [PhotoImage(file='data/search.gif', format=f'gif -index {i}') for i in range(size_gif)]

    def update(index):
        if gif_key:
            frame = frames[index]
            if index == size_gif - 1:
                index = -1
            index += 1
            # lb_gif.configure(image=frame, bd=0)
            btn_start.config(image=frame, width="130", height="130", bd=0, bg=root['bg'], activebackground=root['bg'])
            root.after(45, update, index)

    # lb_gif.place(x=230, y=300)
    root.after(0, update, 0)


def start_stop_app():
    global FINDER_KEY, gif_key, btn_start
    btn_text = btn_start['text']

    if btn_text == "Старт":
        if not lb_path_all[0] or not lb_path_all[1]:
            messagebox.showerror(title="Error",
                                 message=f"Надо сначала выбрать изображение окна контроля и его кнопки!")
            return
        btn_start['text'] = "Стоп"
        for btn in btn_all:
            btn['state'] = 'disabled'
        display_report('The program is started\n')
        FINDER_KEY = True
        try:
            thread = threading.Thread(target=run_search_algorithm, daemon=True)
            thread.start()
            gif_key = True
            display_gif()
        except Exception as exp:
            report_bug(exp)

    elif btn_text == "Стоп":
        btn_start.destroy()
        btn_start = Button(root, text="Старт", font=('Arial', 16, 'italic', 'bold'), command=start_stop_app,
                           activeforeground="blue",
                           activebackground="pink", bg='red', bd=5, width=12, height=2)
        btn_start.place(relx=0.5, rely=0.75, anchor=N)
        gif_key = False
        FINDER_KEY = False
        btn_start['text'] = "Старт"
        for btn in btn_all:
            btn['state'] = 'normal'
        display_report('The program is stopped\n')
        # lb_gif.destroy()


def choose_img_file(index: int) -> None:
    global lb_path_all
    if lb_path_all[index]:
        lb_path_all[index].destroy()
        lb_path_all[index] = None
    file_path = get_img_path()
    if not file_path:
        return
    text = f"Path: '{file_path}'"
    lb_path_all[index] = Label(master=root, text=text, font=('Comic Sans MC', 12), fg='coral4',
                               justify=LEFT)  # , wraplength=390
    if index == 0:
        lb_path_all[0].place(x=20, y=140, anchor=W)
        shutil.copyfile(file_path, IMG_CONTROL_WINDOW)
        display_report('Choose img control window')
    elif index == 1:
        lb_path_all[1].place(x=20, y=230, anchor=W)
        shutil.copyfile(file_path, IMG_CONTROL_BUTTON)
        display_report('Choose img control button')
    elif index == 2:
        lb_path_all[2].place(x=20, y=320, anchor=W)
        shutil.copyfile(file_path, IMG_EXIT_WINDOW)
        display_report('Choose img exit window')
    elif index == 3:
        lb_path_all[3].place(x=20, y=410, anchor=W)
        shutil.copyfile(file_path, IMG_EXIT_BUTTON)
        display_report('Choose img exit button')
    long_line_wrap(lb_path_all[index], text)


def add_objects() -> None:
    global btn_all, btn_start
    lb_title = Label(text="Choose Screens", font=('Times', 22, 'italic', 'bold'), fg='magenta')
    lb_title.place(relx=0.5, rely=0.01, anchor=N)
    lb_delimiter = Label(text=f"{'-' * 80}", font=('Times', 20), fg='cyan')
    lb_delimiter.place(relx=0.5, rely=0.06, anchor=N)
    lb_cw = Label(master=root, text="Control window:", font=('Comic Sans MC', 15))
    lb_cb = Label(text="Control button:", font=('Comic Sans MC', 15))
    lb_ew = Label(text="Exit window:", font=('Comic Sans MC', 15))
    lb_eb = Label(text="Exit button:", font=('Comic Sans MC', 15))
    lb_cw.place(x=10, y=100, anchor=W)
    lb_cb.place(x=10, y=190, anchor=W)
    lb_ew.place(x=10, y=280, anchor=W)
    lb_eb.place(x=10, y=370, anchor=W)
    btn_cw = Button(root, text="Выбрать", command=lambda: choose_img_file(0), activeforeground="blue",
                    activebackground="pink")
    btn_cb = Button(root, text="Выбрать", command=lambda: choose_img_file(1), activeforeground="blue",
                    activebackground="pink")
    btn_ew = Button(root, text="Выбрать", command=lambda: choose_img_file(2), activeforeground="blue",
                    activebackground="pink")
    btn_eb = Button(root, text="Выбрать", command=lambda: choose_img_file(3), activeforeground="blue",
                    activebackground="pink")
    btn_cw.place(x=200, y=100, anchor=CENTER)
    btn_cb.place(x=190, y=190, anchor=CENTER)
    btn_ew.place(x=180, y=280, anchor=CENTER)
    btn_eb.place(x=170, y=370, anchor=CENTER)
    btn_all = [btn_cw, btn_cb, btn_ew, btn_eb]
    btn_start = Button(root, text="Старт", font=('Arial', 16, 'italic', 'bold'), command=start_stop_app,
                       activeforeground="blue",
                       activebackground="pink", bg='red', bd=5, width=12, height=2)
    btn_start.place(relx=0.5, rely=0.75, anchor=N)


def sound_notification(words: str) -> None:
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 180)  # setting up new voice rate
        engine.setProperty('volume', 0.8)  # setting up volume level  between 0 and 1
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
        engine.say(words)
        engine.runAndWait()
    except Exception as exp:
        report_bug(exp)


def report_to_file(file_name: str, text_report: str) -> None:
    with open(file=file_name, mode="w", encoding="utf-8") as file:
        file.write(text_report)


def report_bug(exp: Exception) -> None:
    global BUGS_STR
    today = datetime.today()
    date_y, date_m, date_d = today.year, today.month, today.day
    time_h, time_m, time_s = today.hour, today.minute, today.second
    if time_s < 10:
        time_s = f"0{time_s}"
    bug = f"{type(exp).__name__}: {type(exp)} -> {exp} -> {exp.__suppress_context__=}; {exp.__traceback__}; {type(exp).__annotations__=}"
    report = f"{date_d}.{date_m}.{date_y} {time_h}:{time_m}:{time_s} -> {bug}"
    BUGS_STR += f"{report}\n"
    display_report('Error!')
    report_to_file(NAME_BUGS_FILE, BUGS_STR)


def display_report(mes: str) -> None:  # Add logger?
    global REPORT_STR
    today = datetime.today()
    date_y, date_m, date_d = today.year, today.month, today.day
    time_h, time_m, time_s = today.hour, today.minute, today.second
    if time_s < 10:
        time_s = f"0{time_s}"
    report = f"{date_d}.{date_m}.{date_y} {time_h}:{time_m}:{time_s} -> {mes}"
    # print(report)
    REPORT_STR += f"{report}\n"
    report_to_file(NAME_REPORT_FILE, REPORT_STR)


def finder_close_window() -> int:
    display_report("Start finder_close_window")
    while FINDER_KEY:
        find_exit_window = pg.locateOnScreen(IMG_EXIT_WINDOW, confidence=CONFIDENCE_VAL)
        tm.sleep(1)

        if find_exit_window:
            sound_notification("The closing window is found!")
            display_report(f"{find_exit_window=}")
            tm.sleep(SLEEP_TIME_SEC)
            pg.moveTo(find_exit_window, duration=DURATION_MOVE)
            tm.sleep(SLEEP_TIME_SEC)
            find_exit_button = pg.locateOnScreen(IMG_EXIT_BUTTON, confidence=CONFIDENCE_VAL, region=find_exit_window)
            if find_exit_button:
                sound_notification("Closing it!")
                display_report(f"{find_exit_button=}")
                tm.sleep(SLEEP_TIME_SEC)
                pg.moveTo(find_exit_button, duration=DURATION_MOVE)
                tm.sleep(SLEEP_TIME_SEC)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(SLEEP_TIME_SEC)
                display_report("finder_close_window done!\n")
                return 1
        tm.sleep(1)


def finder_control_window() -> int:
    display_report("Start finder_control_window")
    while FINDER_KEY:
        find_control_window = pg.locateOnScreen(IMG_CONTROL_WINDOW, confidence=CONFIDENCE_VAL)
        tm.sleep(1)

        if find_control_window:
            sound_notification("The control window is found!")
            display_report(f"{find_control_window=}")
            tm.sleep(SLEEP_TIME_SEC)
            pg.moveTo(find_control_window, duration=DURATION_MOVE)
            tm.sleep(SLEEP_TIME_SEC)
            find_control_button = pg.locateOnScreen(IMG_CONTROL_BUTTON, confidence=CONFIDENCE_VAL,
                                                    region=find_control_window)
            if find_control_button:
                sound_notification("Closing it!")
                display_report(f"{find_control_button=}")
                tm.sleep(SLEEP_TIME_SEC)
                pg.moveTo(find_control_button, duration=DURATION_MOVE)
                tm.sleep(SLEEP_TIME_SEC)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(SLEEP_TIME_SEC)

                if lb_path_all[2] and lb_path_all[3]:
                    display_report("finder_control_window done!")
                    return finder_close_window()
                else:
                    display_report("finder_control_window done!\n")
                    return 1
        tm.sleep(1)


def run_search_algorithm() -> None:
    global TOTAL_COUNT_CONTROL
    display_report(f"Start thread {threading.currentThread()}; Name: {threading.currentThread().getName()}")
    while FINDER_KEY:
        if finder_control_window():
            TOTAL_COUNT_CONTROL += 1
        else:
            break
    display_report(f"Count start control = {TOTAL_COUNT_CONTROL}")
    display_report(f"Thread {threading.currentThread()} done.\n")


if __name__ == "__main__":
    # print("The program for auto-marking on the webinar\n")
    try:
        create_dir()
        root = Tk()
        set_configure()
        set_sizes()
        add_objects()
        root.mainloop()
    except Exception as ex:
        report_bug(ex)
