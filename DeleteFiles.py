import os
import stat
import time

from colorama import Fore, Style, init

init(autoreset=True)

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
    a = '\nThank you for using our product!\nHave a nice day!\n'
    for i in a:
        print(GREEN + i, end='')
        time.sleep(0.025)  # Приостановить выполнение программы
    time.sleep(10)
    exit()


def delete_files(dir_path):
    # os.walk() # Идет вглубь каталогов
    total_files = len(os.listdir(dir_path))
    yellow_out(f'List of files: {os.listdir(dir_path)}')
    yellow_out(f'Total files: {len(os.listdir(dir_path))}\n')

    type_file = input('Type of file to delete: ').lower().strip()
    if type_file[0] != '.':
        type_file = '.' + type_file
    yellow_out(f'Type of file to delete: {type_file}\n')

    file_count = 0
    count_done_files, count_error_files = [], []
    for file in os.listdir(dir_path):
        file_count += 1
        if file[file.rfind('.'):].lower() == type_file:
            try:
                os.chmod(os.path.join(dir_path, file), stat.S_IWRITE)  # Не удаляет без этого
                os.remove(os.path.join(dir_path, file))
                done_out(f'\tCount {file_count}/{total_files}:  File "{file}" was deleted!\tstatus: Done')
                count_done_files.append(file)
            except Exception as e:
                error_out(f"\n\tError:\n\tType: {type(e)}\n\tName: {type(e).__name__} was raised: {e}\n")
                error_out(f'\tCount {file_count}/{total_files}:  File "{file}" could not be deleted!\tstatus: Error')
                count_error_files.append(file)
        else:
            yellow_out(f'\tCount {file_count}/{total_files}:  File "{file}" has a different format!\tstatus: Skip')

    done_out(f'\nList of files x{len(os.listdir(dir_path))}: {os.listdir(dir_path)}')
    done_out(f'Deleted files x{len(count_done_files)}: {count_done_files}')
    done_out(f'Not deleted files x{len(count_error_files)}: {count_error_files}')
    done_out(f'Missing files: {total_files - len(count_error_files) - len(count_done_files)}')
    done_out('\tDone!')


def main():
    while True:
        dir_path = input("Path to the directory: ")
        if os.path.exists(dir_path):
            done_out(f"Path: '{dir_path}' status: OK")
            delete_files(dir_path)
            break
        else:
            error_out(f"Path: '{dir_path}' status: Not found")
            error_out(f"Пути '{dir_path}' не существует, введите другой!\n")

    exi_t()


if __name__ == '__main__':
    hello = YELLOW + " A program for deleting files " + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')
    print(f'Current Working Directory is: {os.getcwd()}\n')
    main()
