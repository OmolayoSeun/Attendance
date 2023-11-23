from tkinter import Frame, Button, Entry, Label
from resources.Colors import Color as color
import tkinter as tk

def configFrame(frame: Frame):
    frame.config(
        background=color.white
    )
    pass


def configLabel(item: Label):
    item.config(
        background=color.white
    )
    return item


def configEntry(item: Entry, textHint: str):
    #item.config(border=1, background=color.white)
    item.insert(0, textHint)
    pass


def configButton(item: Button):
    item.config(
        background=color.skyBlue, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.skyBlue,
    )
    pass


def configDefBtn(item: Button):
    item.config(
        background=color.skyBlue, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.skyBlue,
    )
    return item

def add_hint(entry, hint_text):
    def on_entry_click(event):
        if entry.get() == hint_text:
            entry.delete(0, tk.END)
            entry.configure(foreground='black')  # Change text color to black

    def on_focusout(event):
        if entry.get() == '':
            entry.insert(0, hint_text)
            entry.configure(foreground='grey')  # Change text color to grey

    entry.insert(0, hint_text)
    entry.configure(foreground='grey')  # Set default text color to grey
    entry.bind('<FocusIn>', on_entry_click)
    entry.bind('<FocusOut>', on_focusout)