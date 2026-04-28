import requests
import tkinter as tk

""" def Trees(tree):
    response = requests.get(f"https://data.cityofnewyork.us/resource/uvpi-gqnh.json?tree_id={tree}")
    data = response.json()
    return data

tree = Trees("199062")
print(tree[0]["spc_common"]) """

window = tk.Tk()
window.title("tree !! !!! !")
window.geometry("600x450")
data_type = tk.StringVar()
inp = tk.StringVar()
label = tk.Label(window, font=("Comic Sans MS", 10), text="enter the data you would like to access:\n\nTree ID, Block ID, Status, Scientific name, Common name, Zip code")
label.pack(pady=10)
entry=tk.Entry(window, textvariable = data_type, font=("Comic Sans MS", 10), width=30)
entry.pack(pady=5)

def search():
    dtype = data_type.get()
    print(f"Searched for {dtype}")

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
