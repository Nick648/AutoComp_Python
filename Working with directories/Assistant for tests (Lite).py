import os
from datetime import datetime

# Consts for time and date
today = datetime.today()
date_y, date_m, date_d = today.year, today.month, today.day
# time_h, time_m, time_s = today.hour, today.minute, today.second

# Consts way
DESKTOP_DIR = os.path.expanduser('~') + r'\Desktop'
DIRS_NAME = f'Tests {date_d}_{date_m}_{str(date_y)[-2:]}'
DIRS_WAY = os.path.join(DESKTOP_DIR, DIRS_NAME)
ENCODE = 'utf-8'
DIR_PATH = ''
FILE_PATH = ''
FILE_PATH_A = ''
FILE_PATH_Q = ''
FILE_PATH_U = ''
FILE_NAME = ''
KEY_EXIT = ['quit', 'quit()', 'exit', 'exit()', '!q']
if not os.path.exists(DIRS_WAY):
    os.mkdir(DIRS_WAY)
    print(f'Dir "{DIRS_WAY}" created!')


def update_paths(dir_name):
    global DIR_PATH, FILE_PATH, FILE_NAME, FILE_PATH_A, FILE_PATH_Q, FILE_PATH_U
    DIR_PATH = os.path.join(DIRS_WAY, dir_name)

    FILE_PATH = os.path.join(DIR_PATH, dir_name + '.txt')
    # FILE_NAME = FILE_PATH[FILE_PATH.rfind('\\') + 1:]
    # only_path = os.path.dirname(FILE_PATH)
    # DIR_NAME, FILE_NAME = os.path.split(FILE_PATH)
    FILE_NAME = os.path.basename(FILE_PATH)

    file_name_a = FILE_PATH[:FILE_PATH.rfind('.')] + '_A.txt'
    FILE_PATH_A = os.path.join(DESKTOP_DIR, file_name_a)

    file_name_q = FILE_PATH[:FILE_PATH.rfind('.')] + '_Q.txt'
    FILE_PATH_Q = os.path.join(DESKTOP_DIR, file_name_q)

    file_name_u = FILE_PATH[:FILE_PATH.rfind('.')] + '_U.txt'
    FILE_PATH_U = os.path.join(DESKTOP_DIR, file_name_u)


def change_paths():
    while True:
        print(f'\nChange path.\t* For exit enter: {KEY_EXIT}')
        file_dir_name = input('Name dir/file for change: ').strip()
        if file_dir_name in KEY_EXIT:
            return
        if file_dir_name[-4:] != '.txt':
            file_dir_name += '.txt'
        update_paths(file_dir_name[:-4])

        if os.path.exists(FILE_PATH):
            print(f'\nPath "{DIR_PATH}" changed!')
            return


def display_paths():
    print('\n\tConsts:')
    print(f'{DIR_PATH=};')
    print(f'{FILE_NAME=};')
    print(f'{FILE_PATH=};')
    print(f'{FILE_PATH_A=};')
    print(f'{FILE_PATH_Q=};')
    print(f'{FILE_PATH_U=};')
    print('*' * 40)


def create_dir():
    dir_name = input('\nCreate dir with name: ').strip()
    update_paths(dir_name)

    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
        print(f'\nDir "{DIR_PATH}" created!')


def create_file():
    file_name = input('\nCreate file with name: ').strip()
    if file_name[-4:] != '.txt':
        file_name += '.txt'
    update_paths(file_name[:-4])

    if os.path.exists(FILE_PATH):
        print(f'\nFile "{FILE_PATH}" already created!')
        return

    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
        print(f'\nDir "{DIR_PATH}" created!')

    lines = input('Count of lines in file: ').strip()
    try:
        lines = int(lines)
    except Exception as ex:
        print(f'{type(ex).__name__}: {ex}')
        return

    with open(file=FILE_PATH, mode='w', encoding=ENCODE) as file:
        for line in range(1, lines + 1):
            file.write(f'{line}) \n')
    print(f'\nFile "{FILE_PATH}" created!')
    os.startfile(FILE_PATH)


def replace_answers_file():
    while not os.path.exists(FILE_PATH):
        print(f'\nFile "{FILE_PATH}" not exist! \n\t* For exit enter: {KEY_EXIT}')
        file_name = input('Replace answers in file with name: ').strip()
        if file_name in KEY_EXIT:
            return
        if file_name[-4:] != '.txt':
            file_name += '.txt'
        update_paths(file_name[:-4])

    if os.path.exists(FILE_PATH_A):
        print(f'\nFile "{FILE_PATH_A}" already created!')
        return

    with open(file=FILE_PATH, mode='r') as file:  # , encoding=ENCODE
        answers = file.read()
    with open(file=FILE_PATH_A, mode='w', encoding=ENCODE) as file_A:
        for line in answers.strip().split('\n'):
            if line:
                only_ans = line[line.rfind(')') + 2:].strip()
                if only_ans.isdigit():
                    answer_line = line[:line.rfind(' ') + 1] + ','.join(sorted(only_ans))

                    # only_ans = only_ans.replace('1', 'Полностью не согласен').strip()
                    # only_ans = only_ans.replace('2', 'Скорее не согласен').strip()
                    # only_ans = only_ans.replace('3', 'Ни то, ни другое (Нейтрален)').strip()
                    # only_ans = only_ans.replace('4', 'Скорее согласен').strip()
                    # only_ans = only_ans.replace('5', 'Полностью согласен').strip()
                    # answer_line = line[:line.rfind(' ') + 1] + only_ans
                elif '+' in only_ans or '-' in only_ans:
                    answer_line = line.replace('-', 'Нет').replace('+', 'Да').strip()
                file_A.write(f'{answer_line}\n')

    print(f'\nFile "{FILE_PATH_A}" created!')
    os.startfile(FILE_PATH_A)


def unification_question_answer():
    if not os.path.exists(FILE_PATH_A):
        print(f'\nFile "{FILE_PATH_A}" not exist!')
        print(f'Need to perform replace_answers_file. >>>')
        replace_answers_file()
        if not os.path.exists(FILE_PATH_A):
            return
    if not os.path.exists(FILE_PATH_Q):
        print(f'\nFile "{FILE_PATH_Q}" not exist!')
        print(f'Need to add a file with questions')
        return

    if os.path.exists(FILE_PATH_U):
        print(f'\nFile "{FILE_PATH_U}" already created!')
        return

    with open(file=FILE_PATH_Q, mode='r') as file_q:  # , encoding=ENCODE
        questions = file_q.read()
        # print(file_q.encoding)
    with open(file=FILE_PATH_A, mode='r', encoding=ENCODE) as file_a:
        answers = file_a.read()

    questions = questions.strip().split('\n')
    answers = answers.strip().split('\n')

    ratio_lines = int(len(questions) / len(answers))

    with open(file=FILE_PATH_U, mode='w', encoding=ENCODE) as file_U:
        item_q = 0
        for item in range(len(answers)):
            if answers[item] and questions[item_q]:
                only_ans = answers[item][answers[item].find(')') + 2:].strip()
                line_u = f'{questions[item_q]}\n'
                for i in range(ratio_lines-1):
                    item_q += 1
                    line_u += f'{questions[item_q]}\n'
                item_q += 1
                line_u += f'\tОтвет: {only_ans}\n'
                file_U.write(line_u)
    print(f'\nFile "{FILE_PATH_U}" created!')
    os.startfile(FILE_PATH_U)


def txt_to_pdf():  # text file to pdf file
    from fpdf import FPDF
    pdf = FPDF()  # FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open(FILE_PATH_U, "r") as file:  # , encoding=ENCODE
        print(file.encoding)
        text = file.read()
    print(f'TEXT: {text[54:57]}')
    text = text.strip().split('\n')
    for line in text:
        print(line, type(line))
        pdf.cell(200, 10, txt=line, ln=1, align='C')
    pdf.output("my_pdffile.pdf")


if __name__ == '__main__':
    options = '''
    CHOICE: 
        1) create_file;
        2) replace_answers_file;
        3) unification_question_answer;
        4) create_dir;
        5) txt_to_pdf;
        6) change_paths;
        7) display_paths;
        8) Exit;
        P.S. _Q - Questions, _A - Answers, _U - Unification;

    Your answer >>> '''

    while True:
        choice = input(options)
        if choice == '1':
            create_file()
        elif choice == '2':
            replace_answers_file()
        elif choice == '3':
            unification_question_answer()
        elif choice == '4':
            create_dir()
        elif choice == '5':
            txt_to_pdf()
        elif choice == '6':
            change_paths()
        elif choice == '7':
            display_paths()
        elif choice == '8':
            break
        else:
            print(f'Option "{choice}" -> Not Found!')

    print('\nThx for using! Bye!')
