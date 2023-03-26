import requests
import json
# # 61830027-a873-4bec-bc9e-f2fb4f5bd5c0
def get_coordinates(address):
    # url = f"https://geocode-maps.yandex.ru/1.x/?apikey=61830027-a873-4bec-bc9e-f2fb4f5bd5c0&format=json&geocode={address}"
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey=61830027-a873-4bec-bc9e-f2fb4f5bd5c0&format=json&geocode={address}"
    response = requests.get(url)
    json_data = json.loads(response.text)
    print(response)
    print(json_data)
    coordinates = json_data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    longitude, latitude = map(float, coordinates.split())
    return longitude, latitude

if __name__ == "__main__":
    address = "Россия, Московская область, Люберецкий район, Новорязанское шоссе, 23-й километр, СНТ Ручеёк, ул. Весенняя 862"
    get_coordinates(address)
    longitude, latitude = get_coordinates(address)
    print(f"Долгота: {longitude}, Широта: {latitude}")



