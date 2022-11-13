import subprocess


# import os

def check_decode():
    codecs = ["cp1251", "cp1252", "cp866", "utf-16be", "utf-16", "utf-8", "ASCII", "windows-1251", "koi8-r"]
    for code in codecs:
        print(f'\t{code}:')
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode(code, errors='ignore').split('\n')
        print(profiles_data)


def extract_wifi_passwords():
    """Extracting Windows Wi-Fi passwords into .txt file"""

    # HOME_DIR = os.path.expanduser('~') + r'\Desktop'
    # print("Путь к рабочему столу: " + HOME_DIR + "\n")

    try:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode("utf-8").split(
            '\n')  # .decode('utf-8', errors='ignore')
        profiles = [i.split(':')[1].strip() for i in profiles_data if 'All User Profile' in i]
    except UnicodeDecodeError:
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode("cp866").split(
            '\n')  # .decode('cp866', errors='replace')
        profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]

    # for item in profiles_data:
    #    print(item)

    for profile in profiles:
        try:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode(
                'utf-8').split('\n')
        except UnicodeDecodeError:
            profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode(
                'cp866').split('\n')
        except subprocess.CalledProcessError:
            pass
        else:
            pass

        # for item in profile_info:
        #    print(item)

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
        except IndexError:
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
        else:
            password = None

        # print(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}')

        # New file nearly .exe
        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n')

        '''
        # new file with passwords in desktop
        with open(file=HOME_DIR + r'\wifi_passwords_2.txt', mode='a', encoding='utf-8') as file_2:
            file_2.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}\n')
        '''


def main():
    # check_decode()
    extract_wifi_passwords()
    print("Done!")


if __name__ == '__main__':
    main()
