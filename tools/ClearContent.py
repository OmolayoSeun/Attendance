from tkinter import Frame
from resources.Variables import Variables as v


def clear_content():
    # for widget in v.app.winfo_children():
    #     if widget == isOpened:
    #         widget.destroy()
    try:
        v.holdFrameReference.destroy()
    except:
        print("Null View error")

    pass