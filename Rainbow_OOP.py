# Import Tkinter module
from tkinter import *


# Setting up the program window
root = Tk()
root.geometry('250x223+400+100')
root.title('Rainbow colors')
root.iconbitmap('Rainbow.ico')
root.resizable(0, 0)


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


# Creating a button class
class Buttons:

    def __init__(self, root, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.btn = Button(root, bg=hex_color, command=self.change_color)
        self.btn.pack(fill=X)

    def change_color(self):
        label['text'] = self.text_color
        entry.delete(0, END)
        entry.insert(0, self.hex_color)


# Adding a label
label = Label(root)
label.pack(fill=X)


# Adding an entry
entry = Entry(root, justify='center')
entry.pack(fill=X)


# Creating buttons using a for loop and class Buttons
for k, v in colors.items():
    Buttons(root, v, k)


# Launching the program
root.mainloop()
