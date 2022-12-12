# pip install opencv-python qrcode
import qrcode
import cv2
import os
import time

TYPES_FILE = ['.jpg', '.png', '.jpeg']


def creating_qrcode(link='https://github.com/Nick648'):
    filename = "href.png"
    version = 0
    while os.path.exists(filename):
        version += 1
        filename = f"href version=={version}.png"
    try:
        img = qrcode.make(link)
        img.save(filename)
        print(f'QR-code {link} was created and saved in: {os.path.join(os.getcwd(), filename)}')
        time.sleep(1)
        os.startfile(filename)
    except Exception as ex:
        print(f'Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')


def qrcode_reading(filename='href.png'):  # Add .png .jpg format search input client and dir with pics
    if filename[filename.rfind('.'):].lower() not in TYPES_FILE:
        flag = 0
        tries = []
        for postfix in TYPES_FILE:
            if filename.rfind('.') == -1:
                filename += postfix
            else:
                filename = filename[:filename.rfind('.')] + postfix
            tries.append(filename)
            if os.path.exists(filename):
                flag = 1
                break
        if not flag:
            print(f'Files {tries} not exist!')
            return

    try:
        img = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        if not data:
            data = None
        print(f"Message from QR-code: {data}")  # \n bbox: {bbox}\n straight_qrcode: {straight_qrcode}
    except Exception as ex:
        # print(f'Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')
        print(f"Error: Can't recognize QR code! {filename}")


def check_dir_path():
    dir_path = input("\nThe path to the directory with files: ").strip()
    if os.path.exists(dir_path):
        print(f"Path: '{dir_path}' status: OK")
        return dir_path
    else:
        print(f"Path: '{dir_path}' status: Not found")
        return False


def dir_qrcodes_reading(dir_path):
    # os.walk() # Идет вглубь каталогов
    start_dir = os.getcwd()
    print(f'\nList of files: {os.listdir(dir_path)}')
    print(f'Total files: {len(os.listdir(dir_path))}\n')

    file_count, total_files, skipped_files = 0, len(os.listdir(dir_path)), 0
    os.chdir(dir_path)  # Else error in qrcode_reading from cv2
    for file in os.listdir(dir_path):
        file_count += 1
        if file[file.rfind('.'):].lower() in TYPES_FILE:
            print(f'\tFile {file_count}/{total_files}: "{file}" ', end='')
            qrcode_reading(file)  # os.path.join(dir_path, file)
        else:
            print(f'\tFile {file_count}/{total_files}: "{file}" has a different format!\tstatus: Skip')
            skipped_files += 1

    os.chdir(start_dir)  # Return start working dir
    print(f'\nSkipping files: {skipped_files}')
    print('\tDone!')


def main():
    text_1 = '\nEnter the link to the code or just press Enter: '
    text_2 = '\nThe photo of the code should be in the folder next to the program!\n' \
             'Enter the file name or just press Enter: '

    options = '''
        CHOICE: 
            1) creating_qrcode;
            2) qrcode_reading;
            3) dir_qrcodes_reading;
            4) Exit;
        Your answer >>> '''

    while True:
        choice = input(options)
        if choice == '1':
            link = input(text_1)
            if link:
                creating_qrcode(link)
            else:
                creating_qrcode()
        elif choice == '2':
            filename = input(text_2)
            if filename:
                qrcode_reading(filename)
            else:
                qrcode_reading()
        elif choice == '3':
            dir_path = check_dir_path()
            if dir_path:
                dir_qrcodes_reading(dir_path)
        elif choice == '4':
            break
        else:
            print(f'Option "{choice}" -> Not Found!')

    print('\nThx for using! Bye!')


if __name__ == '__main__':
    main()
