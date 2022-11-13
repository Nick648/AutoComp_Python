import pyautogui as pg
import time as tm
import keyboard


pg.FAILSAFE = True
pg.PAUSE = 1.5


def closer():
    while True:
        if keyboard.is_pressed('Esc'):
            print("Exit closer")
            return 0
    
        find_exit = pg.locateOnScreen('data/Exit.jpg', confidence=0.9)
        find_exit_add = pg.locateOnScreen('data/Exit_add.jpg', confidence=0.9)

        if not find_exit == None:
            print("Find_exit:", find_exit)
            tm.sleep(0.5)
            pg.moveTo(find_exit, duration = 0.5)
            find_exit_1 = pg.locateOnScreen('data/Exit_1.jpg', confidence=0.9, region = find_exit)
            if not find_exit_1 == None:
                print("Find_exit_1:", find_exit_1)
                tm.sleep(0.5)
                pg.moveTo(find_exit_1, duration = 0.5)
                tm.sleep(1)
                pg.click(clicks=1, interval=0.2)
                print("Closer done!")
                return 1

    
def finder():
    while True:
        if keyboard.is_pressed('Esc'):
            print("Exit finder")
            return 0
    
        find_control = pg.locateOnScreen('data/Control.jpg', confidence=0.9)
        find_control_add = pg.locateOnScreen('data/Control_add.jpg', confidence=0.9)

        if not find_control == None:
            print("Find_control:", find_control)
            tm.sleep(0.5)
            pg.moveTo(find_control, duration = 0.5)
            find_control_1 = pg.locateOnScreen('data/Control_1.jpg', confidence=0.9, region=find_control)
            if not find_control_1 == None:
                print("Find_control_1:", find_control_1)
                tm.sleep(0.5)
                pg.moveTo(find_control_1, duration = 0.5)
                tm.sleep(1)
                pg.click(clicks=1, interval=0.2)
                print("Finder done!")
                break

    return closer()


if __name__ == "__main__":
    print('hi')
    count_control = 0
    while True:
        if keyboard.is_pressed('Esc'):
            print("Exit main")
            break
        if finder():
            count_control += 1
    print("Count_control:", count_control)
    print("Exit")
    input()
