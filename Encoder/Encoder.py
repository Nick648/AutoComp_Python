import random

SYSTEM_CODES = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Encoder:
    # 'Z' use for space!!! => num_sys(max)=35
    def __init__(self, num_sys: int = -1, code_len: int = 3, ignore_spaces: bool = None, reverse_encoding: bool = None):
        if num_sys != -1:
            self.__num_sys = num_sys
        else:
            self.__num_sys = random.randint(20, 35)

        self.__code_len = code_len

        if ignore_spaces is None:
            self.__ignore_spaces = False
        else:
            self.__ignore_spaces = ignore_spaces

        if reverse_encoding is None:
            self.__reverse_encoding = False
        else:
            self.__reverse_encoding = reverse_encoding

        self.check_parameters("__init__")

    def get_num_sys(self) -> int:
        return self.__num_sys

    def set_num_sys(self, num_sys: int = -1) -> None:
        # num_sys max = 35 (opt [20,35])
        if num_sys != -1:
            self.__num_sys = num_sys
        else:
            self.__num_sys = random.randint(20, 35)
        self.check_parameters("set_num_sys")

    def get_code_len(self) -> int:
        return self.__code_len

    def set_code_len(self, code_len: int = 3) -> None:
        self.__code_len = code_len
        self.check_parameters("set_code_len")

    def get_ignore_spaces(self) -> bool:
        return self.__ignore_spaces

    def set_ignore_spaces(self, ignore_spaces: bool = None) -> None:
        if ignore_spaces is None:
            self.__ignore_spaces = False
        else:
            self.__ignore_spaces = ignore_spaces
        self.check_parameters("set_ignore_spaces")

    def get_reverse_encoding(self) -> bool:
        return self.__reverse_encoding

    def set_reverse_encoding(self, reverse_encoding: bool = None) -> None:
        if reverse_encoding is None:
            self.__reverse_encoding = False
        else:
            self.__reverse_encoding = reverse_encoding
        self.check_parameters("set_reverse_encoding")

    def check_parameters(self, func: str = "check_parameters"):
        if not (isinstance(self.__num_sys, int) and 20 <= self.__num_sys <= 35):
            print(f'ParameterError: {self.__num_sys=} in {func}')
        if not (isinstance(self.__code_len, int) and self.__code_len > 0):
            print(f'ParameterError: {self.__code_len=} in {func}')
        if not isinstance(self.__ignore_spaces, bool):
            print(f'ParameterError: {self.__ignore_spaces=} in {func}')
        if not isinstance(self.__reverse_encoding, bool):
            print(f'ParameterError: {self.__reverse_encoding=} in {func}')

    def translate_into_num_sys(self, dec_num: int) -> str:
        system_number = ""
        while dec_num > 0:
            remainder = dec_num % self.__num_sys  # Получаем остаток от деления на num_sys
            system_digit = SYSTEM_CODES[remainder]  # Получаем num_sys цифру
            system_number = system_digit + system_number  # Добавляем цифру в начало шестнадцатеричного числа
            dec_num //= self.__num_sys  # Выполняем целочисленное деление на num_sys

        return system_number

    def translate_into_dec_sys(self, system_num: str) -> int:
        decimal_number = 0
        power = 0
        # Проходим по каждой цифре числа в обратном порядке
        for i in range(len(system_num) - 1, -1, -1):
            el_code = system_num[i]
            value = SYSTEM_CODES.index(el_code)  # Преобразуем цифру в десятичное значение
            # Умножаем значение на num_sys в соответствующей степени
            decimal_number += value * (self.__num_sys ** power)
            power += 1

        return decimal_number

    def get_code_len_chunks(self, code: str):
        """Produce `n`-character chunks from code"""
        for start in range(0, len(code), self.__code_len):
            yield code[start:start + self.__code_len]

    def encode_message(self, message: str) -> str:
        encode_message = ""
        for element in message:
            if element == " " and self.__ignore_spaces:
                if self.__reverse_encoding:
                    encode_message = " " + encode_message
                else:
                    encode_message += " "
            elif element == " " and not self.__ignore_spaces:
                if self.__reverse_encoding:
                    encode_message = "Z" + encode_message
                else:
                    encode_message += "Z"
            else:
                code_el = self.translate_into_num_sys(ord(element))
                if len(code_el) > self.__code_len:
                    print(f"LENGTH_ERROR: Code len >! {code_el} {len(code_el)} > {self.__code_len}")
                if self.__reverse_encoding:
                    encode_message = code_el.rjust(self.__code_len, '0') + encode_message
                else:
                    encode_message += code_el.rjust(self.__code_len, '0')

        return encode_message

    def decode_message(self, message: str) -> str:
        decode_message = ""
        if self.__ignore_spaces:
            message = message.replace(' ', 'Z')
            message = message.split('Z')
        else:
            message = message.split('Z')
        for element in message:
            for code_chunk in self.get_code_len_chunks(element):
                decode_el = self.translate_into_dec_sys(code_chunk)
                if self.__reverse_encoding:
                    decode_message = chr(decode_el) + decode_message
                else:
                    decode_message += chr(decode_el)
            if self.__reverse_encoding:
                decode_message = " " + decode_message
            else:
                decode_message += " "

        if self.__reverse_encoding:
            return decode_message[1::]
        else:
            return decode_message[:-1:]

    def __str__(self):
        return f"Encoder: num_sys={self.__num_sys}, code_len={self.__code_len}, " \
               f"ignore_spaces={self.__ignore_spaces}, reverse_encoding={self.__reverse_encoding};"


if __name__ == '__main__':
    pass
