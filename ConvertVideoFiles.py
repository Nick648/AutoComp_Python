import os
import time

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


def exi_t():  # Выход из программы
    a = '\nThank you for using our product!\nHave a nice day!\n'
    for i in a:
        print(GREEN + i, end='')
        time.sleep(0.025)  # Приостановить выполнение программы
    time.sleep(10)
    exit()


def convert_with_converter():  # Not work
    from converter import Converter
    conv = Converter()
    convert = conv.convert('test/test1.avi', 'test/test1.mp4', {
        'format': 'mp4',
        'audio': {
            'codec': 'aac',
            'samplerate': 11025,
            'channels': 2
        },
        'video': {
            'codec': 'hevc',
            'width': 720,
            'height': 400,
            'fps': 25
        }})

    for timecode in convert:
        print(f'\rConverting ({timecode:.2f}) ...')


def new_folder(dir_path):  # Creating a new folder for converted videos
    # print("Current directory(startup):", os.getcwd())
    os.chdir(dir_path)
    if os.getcwd() != dir_path:
        yellow_out(f"The current working directory has changed to: {os.getcwd()}")

    name_dir = "new_folder_for_converted_files"
    if not os.path.exists(name_dir):  # Creating a folder for copying files
        os.mkdir(name_dir)

    # print("All folders and files:", os.listdir())
    # new_loc_folder = os.getcwd() + fr'\{name_dir}'
    new_loc_folder = os.path.join(os.getcwd(), name_dir)
    return new_loc_folder


def convert_files(dir_path):  # Video conversion
    # os.walk() # Идет вглубь каталогов
    total_files = len(os.listdir(dir_path))
    yellow_out(f'List of files: {os.listdir(dir_path)}')
    yellow_out(f'Total files: {len(os.listdir(dir_path))}\n')

    new_loc_folder = new_folder(dir_path)

    type_file = input('Type of file to convert: ').lower().strip()
    if type_file[0] != '.':
        type_file = '.' + type_file
    yellow_out(f'Type of file to convert: {type_file}\n')

    file_count = 0
    count_done_files, count_error_files = [], []
    for file in os.listdir(dir_path):
        file_count += 1
        if file[file.rfind('.'):].lower() == type_file:
            name_file = file[:file.rfind('.')] + '.mp4'  # Формат выхода файла надо поменять: ввод пользователем!
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
    done_out(f'Not converted files x{len(count_error_files)}: {count_error_files}')
    done_out(f'Missing files: {total_files - len(count_error_files) - len(count_done_files)}')
    done_out(f'The files are written to: {new_loc_folder}')
    done_out('\tDone!')


def main():
    while True:
        dir_path = input("Path to the directory: ").strip()
        if os.path.exists(dir_path):
            done_out(f"Path: '{dir_path}' status: OK")
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
