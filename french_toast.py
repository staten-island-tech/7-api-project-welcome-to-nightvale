import requests
def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("error fetching data")
        return None
    data = response.json()
    return data

pokemon = getPoke("Bulbasaur")
print(pokemon)

