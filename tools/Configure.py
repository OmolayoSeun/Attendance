from tkinter import Frame, Button, Entry, Label
from resources.Colors import Color as color


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


def configEntry(item: Entry):
    item.config(border=1, background=color.white)
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
