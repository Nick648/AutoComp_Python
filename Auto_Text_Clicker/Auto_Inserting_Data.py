from decouple import config
# Keyboard module in Python
import keyboard
import random

# CONTs
name = config('Name', default='Name')
surname = config('Surname', default='Surname')
middle_name = config('Middle_name', default='Middle_name')
birthdate = config('Birthdate', default='Birthdate')
email = config('Email', default='Email')
phone = config('Phone', default='Phone')
telegram_nik = config('Telegram_nik', default='Telegram_nik')
city = config('City', default='City')


def write_data(data: str) -> None:
    delay = random.randint(20, 150) / 1000
    keyboard.write(text=data, delay=delay)


# CONSTs Hotkeys
keyboard.add_hotkey('alt + n', lambda: write_data(name))
keyboard.add_hotkey('alt + s', lambda: write_data(surname))
keyboard.add_hotkey('alt + m', lambda: write_data(middle_name))
keyboard.add_hotkey('alt + b', lambda: write_data(birthdate))
keyboard.add_hotkey('alt + e', lambda: write_data(email))
keyboard.add_hotkey('alt + p', lambda: write_data(phone))
keyboard.add_hotkey('alt + t', lambda: write_data(telegram_nik))
keyboard.add_hotkey('alt + c', lambda: write_data(city))

if __name__ == '__main__':
    print('\tPress "ctrl + esc" to end the program!')
    keyboard.wait('ctrl + esc')
