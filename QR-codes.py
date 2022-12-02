# pip install opencv-python qrcode
import qrcode
import cv2
import os


def creating_qrcode(link='https://github.com/Nick648'):
    filename = "href.png"
    version = 0
    while os.path.exists(filename):
        version += 1
        filename = f"href version=={version}.png"
    try:
        img = qrcode.make(link)
        img.save(filename)
        print(f'{link} was created and saved in: {os.path.join(os.getcwd(), filename)}')
    except Exception as ex:
        print(f'Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')


def qrcode_reading(filename='href.png'):  # Add .png .jpg format search input client and dir with pics
    try:
        img = cv2.imread(filename)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        print(f"Link from QR-code: {data}")  # \nbbox: {bbox}\n straight_qrcode: {straight_qrcode}
    except Exception as ex:
        print(f'Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')


def main():
    text_1 = 'Enter the link to the code or just press Enter: '
    text_2 = 'The photo of the code should be in the folder next to the program!\n' \
             'Enter the file name or just press Enter: '

    options = '''
        CHOICE: 
            1) creating_qrcode;
            2) qrcode_reading;
            3) Exit;
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
            break
        else:
            print(f'Option "{choice}" -> Not Found!')

    print('\nThx for using! Bye!')


if __name__ == '__main__':
    main()
