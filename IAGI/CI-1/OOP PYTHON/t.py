from tkinter import *

window = Tk()
window.title("Values")
window.geometry('350x200')

# Create labels
name_labelA = Label(window, text="Valeur de A")
name_labelA.grid(column=0, row=0, sticky=W)

name_labelB = Label(window, text="Valeur de B")
name_labelB.grid(column=0, row=1, sticky=W)

# Create entries
v1 = StringVar()
name_entryA = Entry(window, textvariable=v1, width=31)  # Set width in Entry, not in grid()
name_entryA.focus_set()
name_entryA.grid(column=1, row=0, sticky=SW, columnspan=1)

v2 = StringVar()
name_entryB = Entry(window, textvariable=v2, width=31)  # Set width in Entry, not in grid()
name_entryB.focus_set()
name_entryB.grid(column=1, row=1, sticky=SW, columnspan=1)

# create buttons : 
plus_button = Button(window, text="+", pady=2)
plus_button.grid(column=1, row=2, sticky=SW, pady=20)

multi_button = Button(window, text="*", pady=2)
multi_button.grid(column=1, row=2, sticky=NE, pady=20)

# Create output label

output_label = Label(window, text="Résultat")
output_label.grid(column=0, row=3, sticky=W)


window.mainloop()
