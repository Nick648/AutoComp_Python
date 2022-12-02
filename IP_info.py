import requests
from pyfiglet import Figlet
import folium
import ipaddress


def display_real_ip():
    import socket
    print('Real IP: ', end='')
    print(socket.gethostbyname(socket.gethostname()))  # YOUR IP


def save_map(response):
    try:
        location = [response.get('lat'), response.get('lon')]
        area = folium.Map(location=location, zoom_start=14)
        folium.Marker(location=location, popup=response.get('query'), tooltip='Your IP').add_to(area)
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        print(f'\n{response.get("query")}_{response.get("city")}.html was created and saved!')
    except Exception as ex:
        print(f'\nName: {type(ex).__name__}; type: {type(ex)} -> {ex}')
        print('The map cannot be created! :(')


def check_own_ip():
    try:
        response = requests.get(url=f'http://ipinfo.io/json/').json()
        # print(response)

        data = {
            '[IP]': response.get('ip'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('region'),
            '[City]': response.get('city'),
            '[Loc]': response.get('loc'),
            '[Org]': response.get('org'),
            '[Postal]': response.get('postal'),
            '[Timezone]': response.get('timezone'),
        }

        print('Info about your ip: ')
        display_real_ip()

        for key, value in data.items():
            print(f'\t{key} : {value}')

        # save_map(response)

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def get_info_by_ip(ip=''):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        print(f'\nInfo about "{ip}" ip: ')
        for key, value in data.items():
            print(f'\t{key} : {value}')

        save_map(response)

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print(f"IP address {address} is valid! The object returned is {ip}")
        return True
    except ValueError:
        print(f"IP address {address} is not valid!")
        return False


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))

    check_own_ip()
    ip = input('\nPlease enter a target IP: ').strip()
    if validate_ip_address(ip):
        get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
