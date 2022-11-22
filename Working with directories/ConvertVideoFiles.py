import os
import time
import datetime
import moviepy.editor as moviepy
# Import everything needed to edit video clips
# from moviepy.editor import *

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


# Consts for time and date
today = datetime.datetime.today()
date_y, date_m, date_d = today.year, today.month, today.day

OUTPUT_FORMAT_VIDEO = '.mp4'


def exi_t():  # Выход из программы
    a = '\nThank you for using our product!\nHave a nice day!\n'
    for i in a:
        print(GREEN + i, end='')
        time.sleep(0.025)  # Приостановить выполнение программы
    time.sleep(7)
    exit()


def new_folder(dir_path):  # Creating a new folder for converted videos
    if os.getcwd() != dir_path:
        os.chdir(dir_path)
        yellow_out(f"The current working directory has changed to: {os.getcwd()}")

    name_dir = f"Converted_files {date_d}_{date_m}_{date_y}"
    if not os.path.exists(name_dir):  # Creating a folder for copying files
        os.mkdir(name_dir)

    # If the folder is created, an additional one will be created with the version specified
    else:
        version = 1
        while os.path.exists(name_dir):
            name_dir = f'Converted_files {date_d}_{date_m}_{date_y} version=={version}'
            version += 1
        os.mkdir(name_dir)

    new_loc_folder = os.path.join(os.getcwd(), name_dir)
    return new_loc_folder


def convert_files(dir_path):  # Video conversion
    # os.walk() # Идет вглубь каталогов
    total_files = len(os.listdir(dir_path))
    yellow_out(f'List of files: {os.listdir(dir_path)}')
    yellow_out(f'Total files: {len(os.listdir(dir_path))}\n')

    new_loc_folder = new_folder(dir_path)

    type_file = input('Type of file to convert: ').strip().lower()
    if type_file[0] != '.':
        type_file = '.' + type_file
    yellow_out(f'Type of file to convert: {type_file}\n')

    file_count, total_files = 0, len(os.listdir(dir_path))
    count_done_files, count_error_files = [], []
    for file in os.listdir(dir_path):
        file_count += 1
        if file[file.rfind('.'):].lower() == type_file:
            name_file = file[:file.rfind('.')] + OUTPUT_FORMAT_VIDEO  # Формат выхода файла: ввод пользователем!
            try:
                clip = moviepy.VideoFileClip(os.path.join(dir_path, file))
                clip.write_videofile(os.path.join(new_loc_folder, name_file))
                done_out(f'\tCount {file_count}/{total_files}:  File "{file}" was converted!\tstatus: Done')
                count_done_files.append(file)
            except OSError:  # Exception as e:
                # error_out(f"\n\tError:\n\tType: {type(e)}\n\tName: {type(e).__name__} was raised: {e}\n")
                error_out(f'\tCount {file_count}/{total_files}:  File "{file}" could not be converted!\tstatus: Error')
                count_error_files.append(file)
        else:
            yellow_out(f'\tCount {file_count}/{total_files}:  File "{file}" has a different format!\tstatus: Skip')

    done_out(f'\nList of files x{len(os.listdir(dir_path))}: {os.listdir(dir_path)}')
    done_out(f'Converted files x{len(count_done_files)}: {count_done_files}')
    done_out(f'Not converted files(Errors) x{len(count_error_files)}: {count_error_files}')
    done_out(f'Skipping files: {total_files - len(count_error_files) - len(count_done_files)}')
    done_out(f'The files are written to: {new_loc_folder}')
    done_out('\tDone!')


def main():
    while True:
        dir_path = input("The path to the directory with files: ").strip()
        if os.path.exists(dir_path):
            done_out(f"Path: '{dir_path}' status: OK\n")
            convert_files(dir_path)
            break
        else:
            error_out(f"Path: '{dir_path}' status: Not found")
            error_out(f"Пути '{dir_path}' не существует, введите другой!\n")

    exi_t()


if __name__ == '__main__':
    hello = YELLOW + " A program for convert video files to mp4" + RESET
    print("\n", "{:*^75}".format(hello), "\n", sep='')
    print(f'Current Working Directory is: {os.getcwd()}\n')
    main()
