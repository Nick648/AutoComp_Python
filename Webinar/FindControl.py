import pyautogui as pg
import time as tm
import keyboard
from datetime import datetime

pg.FAILSAFE = True
pg.PAUSE = 1.5


def display_report(mes: str) -> None:
    today = datetime.today()
    date_y, date_m, date_d = today.year, today.month, today.day
    time_h, time_m, time_s = today.hour, today.minute, today.second
    print(f"{date_d}.{date_m}.{date_y} {time_h}:{time_m}:{time_s} -> {mes}")


def finder_close_window():
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit closer")
            return 0

        find_exit = pg.locateOnScreen('data/Exit.jpg', confidence=0.9)
        # find_exit_add = pg.locateOnScreen('data/Exit_add.jpg', confidence=0.9)
        tm.sleep(1)

        if find_exit:
            display_report(f"{find_exit=}")
            tm.sleep(0.5)
            pg.moveTo(find_exit, duration=0.5)
            tm.sleep(0.5)
            find_exit_1 = pg.locateOnScreen('data/Exit_1.jpg', confidence=0.9, region=find_exit)
            if find_exit_1:
                display_report(f"{find_exit_1=}")
                tm.sleep(0.5)
                pg.moveTo(find_exit_1, duration=0.5)
                tm.sleep(0.5)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(0.5)
                display_report("Closer done!")
                return 1
        tm.sleep(1)


def finder_control_window():
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit finder")
            return 0

        find_control = pg.locateOnScreen('data/Control.jpg', confidence=0.9)
        # find_control_add = pg.locateOnScreen('data/Control_add.jpg', confidence=0.9)
        tm.sleep(1)

        if find_control:
            display_report(f"{find_control=}")
            tm.sleep(0.5)
            pg.moveTo(find_control, duration=0.5)
            tm.sleep(0.5)
            find_control_1 = pg.locateOnScreen('data/Control_1.jpg', confidence=0.9, region=find_control)
            if find_control_1:
                display_report(f"{find_control_1=}")
                tm.sleep(0.5)
                pg.moveTo(find_control_1, duration=0.5)
                tm.sleep(0.5)
                pg.click(clicks=1, interval=0.2)
                tm.sleep(0.5)
                display_report("Finder done!")
                break
        tm.sleep(1)

    return finder_close_window()


if __name__ == "__main__":
    print('hi')
    count_control = 0
    while True:
        if keyboard.is_pressed('Esc'):
            display_report("Exit main")
            break
        if finder_control_window():
            count_control += 1
    print(f"-------> {count_control=}")
    display_report("Exit")
    input()
