from colorama import Fore, init
from Encoder import Encoder

init(autoreset=True)


def auto_test_encoder() -> None:
    test_mes = ''' Привет меня зовут Ник! И мне 172 года. 
    Hi! My name is Nik and I'm 172 years old.
    \t-\_(-_-)_/- '~ёёёёооооууу~' | "yyyyooouuuueeee"
    '''
    print(f"{test_mes=}")
    print(f"Test message:\n{test_mes}")

    def set_coder_test(i: int = 0) -> None:
        values = [(False, False), (True, False), (False, True), (True, True)]
        coder.set_ignore_spaces(values[i][0])
        coder.set_reverse_encoding(values[i][1])
        print(coder)

    coder = Encoder()
    pass_test = 0
    for test in range(4):
        print(f'\nTest №{test + 1}:')
        set_coder_test(test)
        code_mes = coder.encode_message(test_mes)
        print(f'\t{code_mes=}')
        decode_mes = coder.decode_message(code_mes)
        print(f'\t{decode_mes=}')
        if test_mes == decode_mes:
            print('\tRESULT:', Fore.LIGHTGREEN_EX + 'TRUE')
            pass_test += 1
        else:
            print('\tRESULT:', Fore.LIGHTRED_EX + 'FALSE')
    print(f"\n{pass_test}/4 passed test!")


def manual_input_test() -> None:
    coder = Encoder()
    while True:
        mes = input('>>> ')
        if not mes or mes == "break" or mes == "exit" or mes == "-" or mes == "q":
            break
        code_mes = coder.encode_message(mes)
        print(fr'\t{code_mes=}')
        decode_mes = coder.decode_message(code_mes)
        print(fr'\t{decode_mes=}')
        if mes == decode_mes:
            print('\tRESULT:', Fore.LIGHTGREEN_EX + 'TRUE')
        else:
            print('\tRESULT:', Fore.LIGHTRED_EX + 'FALSE')


if __name__ == '__main__':
    auto_test_encoder()
    # manual_input_test()
