import tkinter as tk


class NewWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("New Window")
        self.geometry("300x200")

        self.label = tk.Label(self, text="This is a new window")
        self.label.pack(pady=20)
