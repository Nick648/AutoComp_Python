import os
import time
from colorama import Fore, Style, init
import shutil

init(autoreset=True)

# Const module colorama
RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
YELLOW = Fore.LIGHTYELLOW_EX
RESET = Style.RESET_ALL


def error_out(s):  # Вывод красного текста
    print(RED + s)


def done_out(s):  # Вывод зелёного текста
    print(GREEN + s)


def yellow_out(s):  # Вывод жёлтого текста
    print(YELLOW + s)


def exi_t():  # Выход из программы
    a = '\nThank you for using our product!\nHave a nice day!\n'
    for i in a:
        print(GREEN + i, end='')
        time.sleep(0.025)  # Приостановить выполнение программы
    time.sleep(7)
    exit()


def copy_paste_files(dir_path_copy, dir_path_paste):
    # os.walk() # Идет вглубь каталогов
    total_files = len(os.listdir(dir_path_copy))
    yellow_out(f'List of files: {os.listdir(dir_path_copy)}')
    yellow_out(f'Total files: {len(os.listdir(dir_path_copy))}\n')

    type_file = input('Type of file to copy: ').strip().lower()
    if type_file[0] != '.':
        type_file = '.' + type_file
    yellow_out(f'Type of file to copy: {type_file}\n')

    file_count = 0
    count_done_files, count_error_files = [], []
    for file in os.listdir(dir_path_copy):
        file_count += 1
        if file[file.rfind('.'):].lower() == type_file:  # JPG == jpg !!!
            try:
                copy_file = os.path.join(dir_path_copy, file)
                paste_file = os.path.join(dir_path_paste, file)
                shutil.copyfile(copy_file, paste_file)  # , follow_symlinks=False (For copy just links)
                done_out(f'\tCount {file_count:3}/{total_files}:  File "{file}" was copied!\tstatus: Done')
                count_done_files.append(file)
            except Exception as ex: # PermissionError
                error_out(f"\n\tError:\tType: {type(ex)}\n\tName: {type(ex).__name__} was raised: {ex}\n")
                error_out(f'\tCount {file_count:3}/{total_files}:  File "{file}" could not be copied!\tstatus: Error')
                count_error_files.append(file)
        else:
            yellow_out(f'\tCount {file_count:3}/{total_files}:  File "{file}" has a different format!\tstatus: Skip')

    done_out(f'\nList of files x{len(os.listdir(dir_path_paste))}: {os.listdir(dir_path_paste)}')
    done_out(f'Copied files x{len(count_done_files)}: {count_done_files}')
    done_out(f'Not copied files(Errors) x{len(count_error_files)}: {count_error_files}')
    done_out(f'Missing files: {total_files - len(count_error_files) - len(count_done_files)}')
    done_out('\tDone!')


def enter_path(mes, past_path=''):
    while True:
        dir_path = input(mes).strip()
        if dir_path == past_path:
            error_out(f'The paths for copying and pasting files should not be equal!\n')
        elif os.path.exists(dir_path):
            done_out(f"Path: '{dir_path}' status: OK")
            return dir_path
        else:
            error_out(f"Path: '{dir_path}' status: Not found")
            error_out(f"Пути '{dir_path}' не существует, введите другой!\n")


def main():
    dir_path_copy = enter_path("The path of the directory, where we copy: ")
    dir_path_paste = enter_path("The path of the directory, where we paste: ", dir_path_copy)
    copy_paste_files(dir_path_copy, dir_path_paste)
    exi_t()


if __name__ == '__main__':
    hello = YELLOW + " A program for copying files of a certain type " + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')
    print(f'Current Working Directory is: {os.getcwd()}\n')
    main()
