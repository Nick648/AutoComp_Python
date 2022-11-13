import pyautogui as pg
import time as tm

pg.FAILSAFE = True
pg.PAUSE = 1.5


def write_in_search_line(i, k):
    pg.typewrite(i, interval=0.18)
    pg.press('enter')
    if k == 1:
        pg.hotkey('ctrl', 't')  # New tab


def main():
    pg.hotkey("winleft")
    write_in_search_line("Google", 0)
    tm.sleep(0.8)

    while True:
        bl = pg.locateOnScreen('data/window.jpg', confidence=0.9)
        if bl:
            pg.moveTo(bl)
            pg.click(clicks=2, interval=0.1)
            break

    write_in_search_line("yandex", 0)

    while True:
        bl = pg.locateOnScreen('data/yan.jpg', confidence=0.9)
        if bl:
            break

    pg.moveTo(1716, 172)
    pg.click()
    pg.hotkey('ctrl', 't')
    write_in_search_line("vk", 1)
    write_in_search_line("youtube", 0)


if __name__ == '__main__':
    main()
