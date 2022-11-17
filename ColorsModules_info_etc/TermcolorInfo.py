# from colorama import init
from termcolor import colored, cprint


# используйте Colorama, чтобы Termcolor работал и в Windows
# init()
# теперь вы можете применять Termcolor для вывода вашего цветного текста

def main_information_module(name_module):
    print(colored(f'\n{name_module.__name__}:', 'red'))
    print(help(name_module))
    print(colored('=' * 100, 'yellow'))


def output_information_module():
    import termcolor
    main_information_module(termcolor)
    main_information_module(colored)
    main_information_module(cprint)


def output_colors_options():
    # Available text colors:
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    print(colored('=' * 100, 'yellow'))
    print(colored("\nAll colors options: \n", 'red'))
    k = 0
    for color in colors:
        k += 1
        print(colored(color, color=color))

    print(f'\n\nCount of colors: {k}')
    print(colored('=' * 100, 'yellow'))


def output_highlights_options():
    # Available text highlights:
    highlights = ['on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']

    print(colored('=' * 100, 'yellow'))
    print(colored("\nAll highlights options: \n", 'red'))
    k = 0
    for highlight in highlights:
        k += 1
        print(colored(highlight, on_color=highlight))

    print(f'\n\nCount of highlights: {k}')
    print(colored('=' * 100, 'yellow'))


def output_attributes_options():
    # Available attributes:
    attributes = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']

    print(colored('=' * 100, 'yellow'))
    print(colored("\nAll attributes options: \n", 'red'))
    k = 0
    for attribute in attributes:
        k += 1
        print(colored(attribute, attrs=list(attribute.split(' '))))  # If just list == ['b','o','l','d']

    print(f'\n\nCount of attributes: {k}')
    print(colored('=' * 100, 'yellow'))


def output_all_text_options():
    # Available text colors:
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    # Available text highlights:
    highlights = ['on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta', 'on_cyan', 'on_white']

    # Available attributes:
    attributes = ['bold', 'dark', 'underline', 'blink', 'reverse', 'concealed']

    k = 0
    for color in colors:
        for highlight in highlights:
            for attribute in attributes:
                k += 1
                name_font = ' '.join([color, highlight, attribute])
                # print(colored(name_font, color=None, on_color=None, attrs=None))
                print(colored(name_font, color=color, on_color=highlight, attrs=list(attribute.split(' '))))

    print(colored('=' * 100, 'yellow'))
    print(f'All count: {k}')
    print(colored('=' * 100, 'yellow'))


if __name__ == '__main__':
    # output_information_module()
    # output_all_text_options()
    output_colors_options()
    output_highlights_options()
    output_attributes_options()
