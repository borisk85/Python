# Import Tkinter package and it's modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


# Setting up the program window
root = Tk()
root.geometry('700x400+400+100')


# Adding a menu
main_menu = Menu(root)
root.config(menu=main_menu)


# Functions for a menu buttons (about, quit, open & save)
def about_program():
    messagebox.showinfo(title='About notepad', message='Program Notepad (version 1.0)')


def notepad_quit():
    answer = messagebox.askokcancel(title='Quit', message='Close the program?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Select a file', filetypes=(('Text files (*.txt)', '*.txt'), ('All files', '*.*')))
    if file_path:
        t.delete('1.0', END)
        t.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Text files (*.txt)', '*.txt'), ('All files', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = t.get('1.0', END)
    f.write(text)
    f.close()


# Menu buttons
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=notepad_quit)
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='About', command=about_program)


# Creating a text area
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)
t = Text(f_text)
t.pack(fill=BOTH, expand=1, side=LEFT)


# Creating a scroll
scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)


# Launching the program
root.mainloop()
