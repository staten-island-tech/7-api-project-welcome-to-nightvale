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
data_type = tk.StringVar()
value = tk.StringVar()
inp = tk.StringVar()
label = tk.Label(window, font=("Comic Sans MS", 10), text="enter the data you would like to access:\n\nTree ID, Block ID, Status, Scientific name, Common name, Zip code")
label.pack(pady=10)
entry=tk.Entry(window, textvariable = data_type, font=("Comic Sans MS", 10), width=30)
entry.pack(pady=5)

def search():
    print("hi")

def next():
    dtype = data_type.get()
    label.config(text=f"enter value for {dtype}", textvariable = value)
    button.config(text="search", command=search, command=button.destroy())

button = tk.Button(window, font=("Comic Sans MS", 10), text="continue", width=15, command=next)
button.pack(pady=5)

window.mainloop()


""" def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("cant divide by 0")
    else:
        print(result) """
