from art import *


def random_line_str():
    for _ in range(20):
        text = art("random")
        print(text)


def random_font():
    for _ in range(30):
        text = text2art("test", "random")
        print(text)


# print(art.help_func())
# print(art.art_list())
def display_all_func():
    print(f"{art.ART_NAMES=}")
    print(f"{art.ASCII_ARTS=}")
    print(f"{art.ART_COUNTER=}")
    print(f"{art.ART_VERSION=}")
    print(f"{art.ASCII_FONTS=}")
    print(f"{art.DECORATION_COUNTER=}")
    print(f"{art.DECORATION_NAMES=}")
    print(f"{art.DEFAULT_FONT=}")
    print(f"{art.FONT_COUNTER=}")
    print(f"{art.FONT_NAMES=}")
    print(f"{art.NON_ASCII_ARTS=}")
    print(f"{art.NON_ASCII_FONTS=}")
    print(f"{art.__version__=}")
    print(f"{art.randart()=}")


# display_all_func()
# random_line_str()
random_font()
tprint("test_rnd-medium", font="rnd-medium")
tprint("test_xl", "rnd-xlarge")
tprint("123", "wizard")
print(decor("barcode_1"))
Response = tsave("art", filename="test.txt", overwrite=True)
