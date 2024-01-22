from tkinter import Frame, Button, Entry, Label
from resources.Colors import Color as color
import tkinter as tk

# Set the default properties of a frame
def configFrame(frame: Frame):
    frame.config(
        background=color.white
    )
    pass

# Set the default properties of a label
def configLabel(item: Label):
    item.config(
        background=color.white, foreground=color.grey,
        font=('ariel', '12', 'normal')
    )
    return item

# Set the default properties of an entry box
def configEntry(item: Entry):
    item.config(border=1, background=color.white)

    pass

# Set the default properties of a button
def configButton(item: Button):
    configDefBtn(item)
    pass

# Set the default properties of a button
def configDefBtn(item: Button):
    def on_enter(event):
        item.config(bg=color.skyBlueHighlight, highlightcolor=color.green)  # Change background color when mouse enters

    def on_leave(event):
        item.config(bg=color.skyBlue, highlightcolor=color.green)

    item.config(
        background=color.skyBlue, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.green,
        cursor="hand2", border=0, height=1, font=('ariel', '12', 'bold')
    )
    item.bind('<Enter>', on_enter)
    item.bind('<Leave>', on_leave)
    return item

# Set the default properties of the delete button
def configDeleteBtn(item: Button):
    def on_enter(event):
        item.config(bg=color.redHighlight, highlightcolor=color.white)  # Change background color when mouse enters

    def on_leave(event):
        item.config(bg=color.red, highlightcolor=color.white)

    item.config(
        background=color.red, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.green,
        cursor="hand2", border=0, height=1, font=('ariel', '12', 'bold')
    )
    item.bind('<Enter>', on_enter)
    item.bind('<Leave>', on_leave)

# Set the default hint properties of an entry box
def add_hint(entry, hint_text):
    def on_entry_click(event):
        if entry.get() == hint_text:
            entry.delete(0, tk.END)
            entry.configure(foreground='black', font=('ariel', '12', "normal"))  # Change text color to black

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, hint_text)
            entry.configure(foreground='grey', font=('ariel', '12', "normal"))  # Change text color to grey

    entry.insert(0, hint_text)
    entry.configure(foreground='grey', font=('ariel', '12', "normal"))  # Set default text color to grey
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)
