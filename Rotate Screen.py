import rotatescreen
import time


def main():
    screen = rotatescreen.get_primary_display()
    start = screen.current_orientation

    for i in range(1, 11):
        a = abs((start - i * 90) % 360)
        # print(a)
        screen.rotate_to(a)
        time.sleep(1)

    screen.rotate_to(0)


if __name__ == '__main__':
    main()
