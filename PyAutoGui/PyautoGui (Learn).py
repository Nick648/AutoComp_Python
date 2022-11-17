import time as tm
import pyautogui as pg

pg.FAILSAFE = True  # Ctrl+C остановка программы
kk = pg.KEYBOARD_KEYS

'''
tm.sleep(1)
print(pg.size())
bl = pg.locateOnScreen('1.png', confidence=0.9)
print(bl)
x = bl.left
y = bl.top
print(x, y)
pg.click(x, y)
'''

'''
# Получение позиции мыши и вывод в консоль

print(pg.position())
'''

'''
pg.click(button='right', clicks=3, interval=0.25)
pg.move(50, 50, duration=0.1)
pg.click() # нажатие мышью в текущей позиции
# тройное нажатие правой кнопкой мыши с паузой в четверть секунды между щелчками
'''

'''
tm.sleep(2)
pg.scroll (100, x = 500, y = 500)   # прокрутить до 10 "кликов"
'''

'''
# Передвижение мыши
pg.move(50, 50, duration=0.5)
pg.moveTo(150, 200, 0.5) # Передвигаем к точке относительно экрана
'''

'''
# Нажатие мышкой по определенной точке

pg.click(769, 101)
pg.doubleclick(769, 101) # двойное нажатие
pg.rightclick(769, 101) # нажатие правой кнопкной мыши
pg.leftclick(769, 101) # нажатие левой кнопкной мыши
'''

'''
# Ввод текста
pg.typewrite("itproger.com")
# Выполнения нажатия на клавишу
pg.typewrite(["enter"])
'''

'''
# Выполнения нажатия на сочетание клавиш
pg.hotkey("winleft")
pg.hotkey("winleft", "up")
pg.hotkey("ctrl", "t")
'''

'''
# Вызов различных всплывающих окон
pg.alert("Окно с информацией", "Название окна", button="Текст на кнопке")
age = pg.prompt("Укажите возраст: ", "Название окна")
print(age)
pg.confirm("Вам больше 18?", "Название окна", ("Да, точно", "Нет"))
pg.password("Введите пароль", "Название окна")
'''

'''
# Создание скриншота
pg.screenshot("yourPic.png")
'''

'''
# Мини программа
website = pg.prompt("Введите название сайта:", "Веб сайт", "https://")
pg.click(769, 101)
pg.typewrite(website)
pg.typewrite(["enter"])
pg.screenshot("yourPic.png")
'''
