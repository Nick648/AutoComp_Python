from pynput import keyboard, mouse


def key_listener():
    # В этом блоке будет работать слушатель событий.
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                break
            else:
                print(f'Получено событие клавиатуры {event}')


def mouse_pos():
    my_mouse = mouse.Controller()

    # Считывание положения указателя
    print(f'Текущее положение указателя: {my_mouse.position}')

    # Установка положения указателя
    my_mouse.position = (10, 20)
    print(f'Указатель перемещен в позицию: {my_mouse.position}')
    my_mouse.position = (737, 331)
    print(f'Указатель перемещен в позицию: {my_mouse.position}')

    # Перемещение указателя относительно текущего положения
    my_mouse.move(5, -5)

    # Прокрутка страницы на 3 шага вниз
    my_mouse.scroll(0, 30)  # Up


def mouse_click():
    my_mouse = mouse.Controller()
    # Нажатие и отпускание левой кнопки мыши
    my_mouse.press(mouse.Button.left)
    my_mouse.release(mouse.Button.left)

    # Двойной клик - отличается от простого нажатия
    my_mouse.click(mouse.Button.left, 2)


def listen_key_out():
    from pynput.keyboard import Key, Listener

    def on_press(key):
        print('{0} pressed'.format(key))

    def on_release(key):
        print('{0} release'.format(key))
        if key == Key.esc:
            # Stop listener
            return False

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def display_info_module():
    import pynput
    print(help(keyboard))
    print(help(mouse))
    print(help(pynput))


def display_info_module_keyboard():
    import keyboard
    from keyboard import _keyboard_event, _keyboard_tests
    print(help(keyboard))
    print(help(_keyboard_event))
    print(help(_keyboard_tests))


if __name__ == '__main__':
    # key_listener()
    mouse_pos()
    # mouse_click()
    listen_key_out()
    # display_info_module()
    # display_info_module_keyboard()
