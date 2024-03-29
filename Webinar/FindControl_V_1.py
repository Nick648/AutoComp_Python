import pyautogui as pg
import time as tm
import keyboard
from datetime import datetime

pg.FAILSAFE = True
pg.PAUSE = 1.5

# Const paths files
IMG_CONTROL_WINDOW = r"data/Control.jpg"
IMG_CONTROL_BUTTON = r"data/Control_button.jpg"
IMG_EXIT_WINDOW = r"data/Exit.jpg"
IMG_EXIT_BUTTON = r"data/Exit_button.jpg"


def display_report(mes: str) -> None:  # Add logger?
    today = datetime.today()
    date_y, date_m, date_d = today.year, today.month, today.day
    time_h, time_m, time_s = today.hour, today.minute, today.second
    print(f"{date_d}.{date_m}.{date_y} {time_h}:{time_m}:{time_s} -> {mes}")


def finder_close_window() -> int:
    display_report("Start finder_close_window")
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit finder_close_window")
            return 0

        find_exit_window = pg.locateOnScreen(IMG_EXIT_WINDOW, confidence=0.9)
        # find_exit_add = pg.locateOnScreen('data/Exit_add.jpg', confidence=0.9)
        tm.sleep(1)

        if find_exit_window:
            display_report(f"{find_exit_window=}")
            tm.sleep(0.5)
            pg.moveTo(find_exit_window, duration=0.5)
            tm.sleep(0.5)
            find_exit_button = pg.locateOnScreen(IMG_EXIT_BUTTON, confidence=0.9, region=find_exit_window)
            if find_exit_button:
                display_report(f"{find_exit_button=}")
                tm.sleep(0.5)
                pg.moveTo(find_exit_button, duration=0.5)
                tm.sleep(0.5)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(0.5)
                display_report("finder_close_window done!\n")
                return 1
        tm.sleep(1)


def finder_control_window() -> int:
    display_report("Start finder_control_window")
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit finder_control_window")
            return 0

        find_control_window = pg.locateOnScreen(IMG_CONTROL_WINDOW, confidence=0.9)
        # find_control_add = pg.locateOnScreen('data/Control_add.jpg', confidence=0.9)
        tm.sleep(1)

        if find_control_window:
            display_report(f"{find_control_window=}")
            tm.sleep(0.5)
            pg.moveTo(find_control_window, duration=0.5)
            tm.sleep(0.5)
            find_control_button = pg.locateOnScreen(IMG_CONTROL_BUTTON, confidence=0.9, region=find_control_window)
            if find_control_button:
                display_report(f"{find_control_button=}")
                tm.sleep(0.5)
                pg.moveTo(find_control_button, duration=0.5)
                tm.sleep(0.5)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(0.5)
                display_report("finder_control_window done!")
                return finder_close_window()
        tm.sleep(1)


def main() -> None:
    count_control = 0
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit main")
            break
        if finder_control_window():
            count_control += 1
        else:
            break
    print(f"-------> {count_control=}")
    display_report("Exit")
    tm.sleep(2)


if __name__ == "__main__":
    print("The program for auto-marking on the webinar\n")
    main()
