import os
import time

from colorama import Fore, Style, init

init(autoreset=True)  # Not need RESET at the end massage

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def error_out(s):  # Вывод красного текста
    print(RED + s, sep='')


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s, sep='')


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s, sep='')


def exi_t():  # Выход из программы
    a = '\nThank you for using our program!\nHave a nice day!\n'
    for i in a:
        print(GREEN + i, end='')
        time.sleep(0.025)  # Приостановить выполнение программы
    time.sleep(5)
    exit()


def display_tree_dir(initial_path, size_dirs):  # Output of the directory tree and percent size
    done_out('\nOutput of the directory tree and their percentage of the total size:\n')
    lower_level = initial_path.count("\\")
    for dir_path, size_dir in size_dirs.items():
        dif_level = dir_path.count("\\") - lower_level
        if dif_level > 0:
            perc_size = "{:.3f}".format(size_dir / size_dirs[initial_path] * 100) + '%'
            indent = '\t' * dif_level
            print(f'{indent}{dir_path}  ->  {YELLOW + perc_size}')
        else:
            print(dir_path)


def get_str_size(size_bytes):  # Return str of different format of size
    size_kilobytes = size_bytes / 1024
    size_megabytes = size_kilobytes / 1024
    size_gigabytes = size_megabytes / 1024

    size_kilobytes = "{:.3f}".format(size_kilobytes)
    size_megabytes = "{:.3f}".format(size_megabytes)
    size_gigabytes = "{:.3f}".format(size_gigabytes)
    return f'{size_bytes} bytes = {size_kilobytes} KB = {size_megabytes} MB = {size_gigabytes} GB'


def display_info_dir_path(dir_path, dir_names, filenames, total_size_dir):  # Output all information dir
    print(f'dir_path: {dir_path}; {type(dir_path)}; {len(dir_path)}')
    print(f'dir_names: {dir_names}; {type(dir_names)}; {len(dir_names)}')
    print(f'filenames: {filenames}; {type(filenames)}; {len(filenames)}')
    print(f'Total_size_dir: {get_str_size(total_size_dir)}')
    yellow_out('*' * 50)


def dir_info(initial_path):  # Main algorithm of program
    format_files, size_dirs = dict(), dict()
    total_files, total_dirs, total_size = 0, 0, 0
    for dir_path, dir_names, filenames in os.walk(initial_path):  # , topdown=False
        total_filenames, total_dir_names, total_size_dir = len(filenames), len(dir_names), 0
        total_files += len(filenames)
        total_dirs += len(dir_names)

        for name in filenames:
            path_name = os.path.join(dir_path, name)
            total_size_dir += os.path.getsize(path_name)  # os.stat(path_name).st_size
            key = name[name.rfind('.'):].lower()
            if key in format_files:
                format_files[key] += 1
            else:
                format_files[key] = 1

        total_size += total_size_dir
        size_dirs[dir_path] = total_size_dir
        display_info_dir_path(dir_path, dir_names, filenames, total_size_dir)  # Output all info

    size_dirs[initial_path] = total_size
    print(f'Total folders: {total_dirs}')
    print(f'Total files: {total_files}\n\tFormats: count.')
    for format_name, count in format_files.items():
        print(f"\t{format_name:5}: {count:7}")
    print(f'Total size: {get_str_size(total_size)}')
    display_tree_dir(initial_path, size_dirs)


def main():  # Start program
    while True:
        initial_path = input("Path to the directory: ").strip()

        if os.path.exists(initial_path):
            done_out(f"Path: '{initial_path}' status: OK\n")
            dir_info(initial_path)
            break
        else:
            error_out(f"Path: '{initial_path}' status: Not found")
            error_out(f"Пути '{initial_path}' не существует, введите другой!\n")
    exi_t()


if __name__ == '__main__':  # Program entry point
    hello = YELLOW + " Program for displaying directory information " + RESET
    print("\n", "{:*^80}".format(hello), "\n", sep='')
    print(f'Current Working Directory is: {os.getcwd()}\n')
    main()
