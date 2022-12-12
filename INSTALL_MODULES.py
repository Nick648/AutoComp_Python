import subprocess
import os

if not os.path.exists('venv'):
    print("\nNo interpreter!\n Add in settings virtualenv!")
    exit()

way = os.path.join(os.getcwd(), r'venv\Scripts\python.exe')
print(f'Way to python.exe: {way}\n')


def generate_req():
    subprocess.check_call([way, '-m', 'pip', 'freeze'])  # 0

    str_bytes = subprocess.check_output([way, '-m', 'pip', 'freeze'])
    modules = str_bytes.decode('utf-8').split('\n')
    print(f'\nTotal modules: {len(modules) - 1}')
    if len(modules) - 1 > 0:
        with open(file='req.txt', mode='w', encoding='utf-8') as file:
            for module in modules:
                file.write(module)
        print(f"\n\t generate_req Done!")
    print('*' * 50)


def install_module(module='mysql-connector-python'):  # Installing the module manually
    subprocess.check_call([way, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([way, '-m', 'pip', 'install', module])
    print(f"\n\t install_module '{module}' Done!")
    print('*' * 50)


def install_modules():  # Module installer from a file
    subprocess.check_call([way, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([way, '-m', 'pip', 'install', '-U', 'pip', 'setuptools'])
    subprocess.check_call([way, '-m', 'pip', 'install', 'matplotlib'])
    subprocess.check_call([way, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    print(f"\n\t install_modules Done!")
    print('*' * 50)


if __name__ == '__main__':
    generate_req()
    # install_module('mysql-connector-python')
    # install_modules()
    print(f"\n{'*' * 20} Done! {'*' * 20}")
