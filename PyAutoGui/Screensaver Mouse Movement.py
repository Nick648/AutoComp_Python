import pyautogui as pg
import time
import random
import keyboard
from tkinter import Tk

# Use Ctrl+D for exit!

pg.FAILSAFE = False
WIDTH, HEIGHT = pg.size()

speed_x, speed_y = 30, 30


def get_size_monitor():
    global WIN_WIDTH, WIN_HEIGHT
    bg_window = Tk()
    bg_window.configure(background="black")
    bg_window.title("Background")
    # bg_window.wm_attributes('-transparentcolor', bg_window['bg'])  # Прозрачное приложение!
    bg_window.attributes('-fullscreen', True)
    WIN_WIDTH = bg_window.winfo_screenwidth()
    WIN_HEIGHT = bg_window.winfo_screenheight()
    bg_window.update()
    # time.sleep(2)
    # bg_window.destroy()


def mouse_move():
    global speed_y, speed_x

    pos_x, pos_y = pg.position()
    if pos_x + speed_x >= WIDTH or pos_x + speed_x <= 0:  # if pos_x + speed_x not in range(0, WIDTH + 1):
        speed_x = -speed_x

    if pos_y + speed_y >= HEIGHT or pos_y + speed_y <= 0:  # if pos_y + speed_y not in range(0, HEIGHT + 1):
        speed_y = -speed_y

    pg.move(speed_x, speed_y, duration=0.05)


def functions_move():
    # pg.moveTo(100, 100, 2, pg.easeInQuad)  # start slow, end fast
    # pg.moveTo(100, 100, 2, pg.easeOutQuad)  # start fast, end slow
    # pg.moveTo(100, 100, 2, pg.easeInOutQuad)  # start and end fast, slow in middle
    # pg.moveTo(100, 100, 2, pg.easeInBounce)  # bounce at the end
    # pg.moveTo(100, 100, 2, pg.easeInElastic)  # rubber band at the end

    time.sleep(1)
    func = [pg.easeInQuad, pg.easeOutQuad, pg.easeInOutQuad, pg.easeInBounce, pg.easeInElastic]
    for i in range(5):
        print(f'{func[i].__name__}:\t{func[i]}:\t{type(func[i])}')
        pg.moveTo(500, 500, 1)
        pg.moveTo(1000, 100, 2, func[i])


def main():
    time.sleep(1)
    pg.moveTo(WIDTH / 2, HEIGHT / 2)
    sp = list()
    for i in range(1, 4):
        # pos_speed = WIDTH * i * 0.01
        pos_speed = HEIGHT * i * 0.01
        sp.append(int(pos_speed))
        sp.append(int(pos_speed * -1))

    # rand_x = random.randint(-290, 290)
    # rand_y = random.randint(-290, 290)
    # pg.moveTo(rand_x, rand_y)

    # red, green, blue = random.random(), random.random(), random.random()
    # ball.color(red, green, blue)
    speed_x = random.choice(sp)
    speed_y = random.choice(sp)
    speed_x, speed_y = 40, 40
    print(speed_x, speed_y)

    while True:
        if keyboard.is_pressed('esc'):
            return
        pos_x, pos_y = pg.position()
        if pos_x + speed_x >= WIDTH or pos_x + speed_x <= 0:  # if pos_x + speed_x not in range(0, WIDTH + 1):
            speed_x = -speed_x

        if pos_y + speed_y >= HEIGHT or pos_y + speed_y <= 0:  # if pos_y + speed_y not in range(0, HEIGHT + 1):
            speed_y = -speed_y

        pg.move(speed_x, speed_y, duration=0.001)  #


if __name__ == '__main__':
    get_size_monitor()
    # functions_move()
    main()
