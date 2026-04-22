import requests
def getPoke(poke):
    response = requests.get(f"https://random-d.uk/api/images/51.jpg{poke.lower()}")
    if response.status_code != 200:
        print("error fetching data")
        return None
    data = response.json()
    return data

pokemon = getPoke("Bulbasaur")
print(pokemon)

