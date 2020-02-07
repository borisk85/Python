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

# Function to change the color after a click
def change_color(text_color, hex_color):
    label['text'] = text_color
    entry.delete(0, END)
    entry.insert(0, hex_color)

# Buttons to represent 7 colors of a rainbow
btn_red = Button(root, bg='red', command=lambda: change_color('Red', '#ff0000')).pack(fill=X)
btn_orange = Button(root, bg='orange', command=lambda: change_color('Orange', '#ff7d00')).pack(fill=X)
btn_yellow = Button(root, bg='yellow', command=lambda: change_color('Yellow', '#ffff00')).pack(fill=X)
btn_green = Button(root, bg='green', command=lambda: change_color('Green', '#00ff00')).pack(fill=X)
btn_indigo = Button(root, bg='indigo', command=lambda: change_color('Indigo', '#0000ff')).pack(fill=X)
btn_blue = Button(root, bg='blue', command=lambda: change_color('Blue', '#007dff')).pack(fill=X)
btn_violet = Button(root, bg='purple', command=lambda: change_color('Violet', '#7d00ff')).pack(fill=X)

# Launching the program
root.mainloop()
