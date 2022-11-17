from colorama import Fore, Style, Cursor, Back, init

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def styles_format():  # Выводы текста возможные
    print(YELLOW + "\n\tAll code format options:")
    for style in range(10):
        for c_text in range(30, 38):
            for c_bg in range(40, 48):
                code = f"033[{style};{c_text};{c_bg}m"
                print(f"\033[{style};{c_text};{c_bg}m Some Text; \033[0m \tCode: \{code}")
    print(f'\tCount format codes: {10 * (38 - 30) * (48 - 40)};')


def main_information_module():
    print(RED + '\tColorama: \n')
    import colorama
    print(help(colorama))


def output_information_module(info, name):
    print(RED + name + ': ', str(info), '\n')
    print(help(info), '\n')


def output_info():
    output_information_module(Fore, 'Fore')
    output_information_module(Style, 'Style')
    output_information_module(Cursor, 'Cursor')
    output_information_module(Back, 'Back')


def output_colors_options():
    print(YELLOW + "\n\tAll colors options:")
    for color, key_color in Fore.__dict__.items():
        # print(color, type(color), Fore.__dict__[color], type(Fore.__dict__[color]))
        print(key_color + f"{color}")  # colors[color]
    print(f'\tCount colors: {len(Fore.__dict__)};')


def output_backs_options():
    print(YELLOW + "\n\tAll backs options:")
    for back, key_back in Back.__dict__.items():
        print(key_back + f"{back}")
    print(f'\tCount backs: {len(Back.__dict__)};')


def output_styles_options():
    print(YELLOW + "\n\tAll styles options:")
    for style, key_style in Style.__dict__.items():
        print(key_style + f"{style}")
    print(f'\tCount styles: {len(Style.__dict__)};')


def output_information_lists_module(module, name):
    print('\n\t', RED + name + ': ')
    print(module)
    print(f'type(module): {type(module)}, len(module): {len(module)}\n')


def output_all_text_options():
    # colors = dict(Fore.__dict__.items())
    # print(colors, type(colors), sep='\n')
    output_information_lists_module(Fore.__dict__, 'Colors')
    output_information_lists_module(Style.__dict__, 'Styles')
    output_information_lists_module(Cursor.__dict__, 'Cursors')
    output_information_lists_module(Back.__dict__, 'Backs')

    # for color in colors:
    # for color in colors.keys():
    k = 0
    print(YELLOW + "\n\tAll options: \n", '\tColor  Back  Style \n')
    for color, key_color in Fore.__dict__.items():
        for back, key_back in Back.__dict__.items():
            for style, key_style in Style.__dict__.items():
                k += 1
                name_font = ' '.join([color, back, style])
                # print(color, type(color), Fore.__dict__[color], type(Fore.__dict__[color]))
                print(key_color + key_back + key_style + f"{name_font}", end='  ')  # colors[color]
            print()
    print(f'\tAll count: {len(Fore.__dict__.items()) * len(Back.__dict__.items()) * len(Style.__dict__.items())};')


if __name__ == '__main__':
    # main_information_module()
    # output_info()
    output_colors_options()
    output_backs_options()
    output_styles_options()
    # styles_format()
    # output_all_text_options()
