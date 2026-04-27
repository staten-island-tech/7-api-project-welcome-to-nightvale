import requests
import tkinter as tk

def Trees(tree):
    response = requests.get(f"https://data.cityofnewyork.us/resource/uvpi-gqnh.json?tree_id={tree}")
    data = response.json()
    return data

tree = Trees("199062")
print(tree[0]["spc_common"])

window = tk.Tk()
window.title("tree !! !!! !")
window.geometry("400x250")
label = tk.Label(window, text="staring ominously")
font=("Comic Sans MS", 12)
label.pack(pady=10)
button = tk.Button(window, text="evil button", width=15, command=window.destroy)
font=("Comic Sans MS", 12)
button.pack()
entry=tk.Entry(window, font=("Comic Sans MS", 12), width=30)
entry.grid(row=0, column=1)
entry.pack(pady=5)

window.mainloop()


""" def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("cant divide by 0")
    else:
        print(result) """
