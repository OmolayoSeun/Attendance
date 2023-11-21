import tkinter as tk
from newwindow import NewWindow


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main Window")
        self.geometry("400x300")

        self.button = tk.Button(self, text="Open New Window", command=self.open_new_window)
        self.button.pack(pady=20)

    def open_new_window(self):
        new_window = NewWindow(self)
        new_window.grab_set()
