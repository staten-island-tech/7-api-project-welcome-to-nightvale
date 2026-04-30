import requests
import tkinter as tk
url = "https://data.cityofnewyork.us/resource/uvpi-gqnh.json"

""" def Trees(tree):
    response = requests.get(f"https://data.cityofnewyork.us/resource/uvpi-gqnh.json?tree_id={tree}")
    data = response.json()

tree = Trees("199062")
print(tree[0]["spc_common"]) """

window = tk.Tk()
window.title("tree !! !!! !")
window.geometry("600x450")

value = tk.StringVar()

label = tk.Label(window, font=("Comic Sans MS", 10), text="enter tree id")
label.pack(pady=10)
val_entry=tk.Entry(window, textvariable = value, font=("Comic Sans MS", 10), width=10)
val_entry.pack(pady=5)

def search():
    treeid = value.get()
    label.config(text=f"Tree #{treeid}\nCommon Name: {url + "?=spc_common"}", anchor="w", justify=tk.LEFT)
    val_entry.destroy()
    button.destroy()

button = tk.Button(window, font=("Comic Sans MS", 10), text="search", width=15, command=search)
button.pack(pady=5)

window.mainloop()


""" def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("cant divide by 0")
    else:
        print(result) """
