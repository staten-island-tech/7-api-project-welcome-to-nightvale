import requests
import tkinter as tk

def Trees(tree):
    response = requests.get(f"https://data.cityofnewyork.us/resource/uvpi-gqnh.json?tree_id={tree}")
    data = response.json()
    return data

tree = Trees("199062")
""" print(tree[0]["spc_common"]) """

window = tk.Tk()
window.title("tree !! !!! !")
w
