import subprocess
import os


def generate_req():
    if not os.path.exists('venv'):
        print("No interpreter!\n Add in settings virtualenv!")
        return

    way = os.path.join(os.getcwd(), r'venv\Scripts\python.exe')
    subprocess.check_call([way, '-m', 'pip', 'freeze'])


def install_modules():  # Module installer from a file
    if not os.path.exists('venv'):
        print("No interpreter!\n Add in settings virtualenv!")
        return

    way = os.path.join(os.getcwd(), r'venv\Scripts\python.exe')
    subprocess.check_call([way, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([way, '-m', 'pip', 'install', '-U', 'pip', 'setuptools'])
    subprocess.check_call([way, '-m', 'pip', 'install', 'matplotlib'])
    subprocess.check_call([way, '-m', 'pip', 'install', '-r', 'requirements.txt'])


if __name__ == '__main__':
    generate_req()
    # install_modules()
    print(f"\n\n{'*' * 20} Done! {'*' * 20}")
