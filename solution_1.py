import requests


def fetch_vehicles():
    vehicles = []
    try:
        URL = "https://swapi.dev/api/vehicles/"
        response = requests.get(url=URL)
        data = response.json()
        vehicles = data["results"][:5]
    except ConnectionError:
        print("The api does not work properly")
    return vehicles


if __name__ == "__main__":
    print(fetch_vehicles())
