import requests
import folium
import os

MOSCOW_KREMLIN = [55.75, 37.6167]
MOSCOW = (55.747592, 37.619908)
PETER = (59.925173, 30.330548)
MAP = folium.Map(location=MOSCOW_KREMLIN, zoom_start=12)


def search_ip_location():
    global MAP
    try:
        response = requests.get(url='http://ipinfo.io/json/').json()
        # print(response)

        loc = response.get('loc')
        ip = response.get('ip')

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

        # print('  Your IP detail')
        # for key, value in data.items():
        #     print(f'\t{key} : {value}')

        # latitude, longitude = list(map(float, loc.split(',')))
        coordinates = list(map(float, loc.split(',')))

        MAP = folium.Map(location=coordinates, zoom_start=12)
        folium.Marker(location=coordinates, popup=ip, tooltip='Your IP').add_to(MAP)

    except Exception as ex:
        print(f'Name: {type(ex).__name__}; type: {type(ex)} -> {ex}')


def add_to_map(location=None, popup='New Place', tooltip='tooltip'):
    if location is None:
        location = MOSCOW_KREMLIN
    folium.Marker(location=location, popup=popup, tooltip=tooltip).add_to(MAP)


def save_map():
    filename = "your_map.html"
    version = 0
    while os.path.exists(filename):
        version += 1
        filename = f"your_map version=={version}.html"
    MAP.save(filename)
    print(f'{os.path.join(os.getcwd(), filename)} was created and saved!')


def distance_on_map(place_1=(55.747592, 37.619908), place_2=(59.925173, 30.330548)):
    from geopy.distance import geodesic
    distance_km = geodesic(MOSCOW, PETER).kilometers
    print(f'Расстояние от Москвы до Питера составляет: {distance_km:.2f} км')

    distance_km = geodesic(place_1, place_2).kilometers
    return f'{distance_km:.2f} km'


def main():
    search_ip_location()

    sparrow_hills = [55.709426, 37.541819]
    sh_tooltip = 'Воробьевы горы (подсказка)'
    folium.Marker(location=sparrow_hills, popup='Воробьевы Горы', tooltip=sh_tooltip).add_to(MAP)

    add_to_map([55.794416, 37.676620], 'парк Сокольники', 'парк Сокольники here')
    add_to_map(MOSCOW_KREMLIN, 'Moscow Kremlin', 'Кремль Москвы')

    distance_on_map()

    save_map()


if __name__ == '__main__':
    main()
