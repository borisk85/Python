# Import Tkinter module
from tkinter import *


# Setting up the program window
root = Tk()
root.geometry('250x223+400+100')
root.title('Rainbow colors')
root.iconbitmap('Rainbow.ico')
root.resizable(0, 0)


# Adding a label
label = Label(root)
label.pack(fill=X)


# Adding an entry
entry = Entry(root, justify='center')
entry.pack(fill=X)


# Creating a colors Dictionary
colors = {
    '#ff0000': 'Red',
    '#ff7d00': 'Orange',
    '#ffff00': 'Yellow',
    '#00ff00': 'Green',
    '#007dff': 'Blue',
    '#0000ff': 'Indigo',
    '#7d00ff': 'Violet'
}


# Creating buttons using a for loop
for k, v in colors.items():
    Button(root, bg=k, command=lambda k=k, v=v: change_color(v, k)).pack(fill=X)


# Function to change the color after a click
def change_color(text_color, hex_color):
    label['text'] = text_color
    entry.delete(0, END)
    entry.insert(0, hex_color)


# Launching the program
root.mainloop()
