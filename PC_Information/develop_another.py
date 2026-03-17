import platform, psutil, socket, uuid, re, wmi
from screeninfo import get_monitors
import subprocess
import re


def humanSize(_bytes):
    suffixes = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ', 'ПБ']
    i = 0
    while _bytes >= 1024 and i < len(suffixes) - 1:
        _bytes /= 1024.
        i += 1
    f = ('%.2f' % _bytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


# OS
def get_os_info():
    print('-' * 15, 'ОС', '-' * 15)
    os = platform.uname()
    host = socket.gethostname()
    print(f'ОС: {os.system} {os.release} ({os.version})')
    print(f'Архитектура: {os.machine}')


# Network
def get_network_info():
    print('-' * 15, 'Сеть', '-' * 15)
    print(f'Имя устройства: {host}')
    print(f'IP-адрес: {socket.gethostbyname(host)}')
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    print(f'MAC-адрес: {mac}')


# CPU
def get_cpu_info():
    # CPU frequencies
    def get_cpu_frequencies():
        print('-' * 15, 'ЦПУ частоты', '-' * 15)
        cpufreq = psutil.cpu_freq()
        print(f"Макс. частота: {cpufreq.max:.2f} Mhz")
        print(f"Мин. частота: {cpufreq.min:.2f} Mhz")
        print(f"Текущая частота: {cpufreq.current:.2f} Mhz")

    # CPU usage
    def get_cpu_usage():
        print('-' * 15, 'ЦПУ использование', '-' * 15)
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i + 1}: {percentage}%")
        print(f"Общая загрузка ЦПУ: {psutil.cpu_percent()}%")

    print('-' * 15, 'ЦПУ', '-' * 15)

    computer = wmi.WMI()
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]

    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)

    print(f"ЦПУ: {format(proc_info.Name)}")
    print(f"Ядра процессора: {cpu_cores}")
    print(f"Потоки процессора: {cpu_threads}")


# Graphics card
def get_graphics_card_info():
    print('-' * 15, 'Видеокарта', '-' * 15)
    print('Видеокарта: {0}'.format(gpu_info.Name))


# Ram
def get_ram_info():
    print('-' * 15, 'ОЗУ', '-' * 15)
    memory = psutil.virtual_memory()
    print(f"Объем: {humanSize(memory.total)}")
    print(f"Доступно: {humanSize(memory.available)}")
    print(f"Используется: {humanSize(memory.used)}")
    print(f"Процент: {memory.percent}%")


# SWAP
def get_swap_info():
    print("-" * 15, "SWAP", "-" * 15)
    swap = psutil.swap_memory()
    print(f"Объем: {humanSize(swap.total)}")
    print(f"Доступно: {humanSize(swap.free)}")
    print(f"Используется: {humanSize(swap.used)}")
    print(f"Процент: {swap.percent}%")


# Disk
def get_disk_info():
    print('-' * 15, 'Disk', '-' * 15)
    disk_partitions = psutil.disk_partitions()
    for partition in disk_partitions:
        print(f"Диск: {partition.device}")
        disk = psutil.disk_usage(partition.mountpoint)
        print(f"    Файловая система: {partition.fstype}")
        print(f"    Объем: {humanSize(disk.total)}")
        print(f"    Используется: {humanSize(disk.used)}")
        print(f"    Доступно: {humanSize(disk.free)}")
        print(f"    Процент: {disk.percent}%")


# Monitor
def get_monitor_info():
    print('-' * 15, 'Monitor', '-' * 15)
    for monitor in get_monitors():
        print(f"{monitor.name}: {monitor.width}x{monitor.height}")  # monitor.name.strip('//.')


def get_another_monitor_info():
    proc = subprocess.Popen(['powershell', 'Get-WmiObject win32_desktopmonitor;'], stdout=subprocess.PIPE)
    print(proc)
    res = proc.communicate()
    print(res)
    monitors = re.findall('(?s)\r\nName\s+:\s(.*?)\r\n', res[0].decode("utf-8"))
    print(monitors)


def main():
    # get_monitor_info()
    get_another_monitor_info()


if __name__ == '__main__':
    main()
