import requests
def Trees(tree):
    response = requests.get(f"https://data.cityofnewyork.us/resource/uvpi-gqnh.json{tree}")
    data = response.json()
    return data

tree = Trees("199062")
print(tree)

