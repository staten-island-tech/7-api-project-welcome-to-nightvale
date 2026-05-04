import requests
import tkinter as tk
url = "https://data.cityofnewyork.us/resource/uvpi-gqnh.json"
#cname = url + "?=spc_common"

""" tree = Trees("180683")
print(tree[0]["spc_common"]) """

window = tk.Tk()
window.title("tree !! !!! !")
window.geometry("400x300")
window.resizable = False
window.configure(bg="#7d8556")
value = tk.StringVar()

""" frame = tk.Frame(window, 
                 width= 394, 
                 height = 296, 
                 bg="#7d8556",)
frame.grid(column=1, row=1, sticky='nsew')
frame.pack(pady = 3) """
label = tk.Label(window, 
                 font=("Comic Sans MS", 11,), 
                 text="enter six digit tree id", 
                 foreground= "#211a11", 
                 background = "#7d8556")
#label.grid(column=1, row=2, sticky='we')
label.pack(pady=10)
val_entry=tk.Entry(window, 
                   textvariable = value, 
                   font=("Comic Sans MS", 10, "bold"), 
                   width=10, 
                   foreground= "#211a11", 
                   background = "#dbd8a0")
#val_entry.grid(column=1, row=1, sticky='we')
val_entry.pack(pady=5)


def trees():
    tree = value.get()
    response = requests.get(f"https://data.cityofnewyork.us/resource/uvpi-gqnh.json?tree_id={tree}")
    data = response.json()
    try:
        print(data[0]["tree_id"])
    except IndexError:
        label.configure(text="Tree not found. \n\n Please enter a valid six digit number")
    else:
        label.configure(text = f"Tree ID= {tree} \n\nCommon name: {data[0]["spc_common"]} \nScientific name: {data[0]["spc_latin"]} \nAddress: {data[0]["address"]}", anchor="w", justify=tk.LEFT)
        val_entry.destroy()
        button.destroy()

""" def search():
    treeid = value.get()
    label = tk.Label(command = Trees, anchor="w", justify=tk.LEFT)
    val_entry.destroy()
    button.destroy() """

button = tk.Button(window, font=("Comic Sans MS", 10), text="search", width=15, command=trees, bg="#dbd8a0", fg="#211a11")
button.pack(pady=5)

window.mainloop()


""" def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("cant divide by 0")
    else:
        print(result) """
