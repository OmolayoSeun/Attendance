import tkinter as tk
from tkinter import ttk


def create_bar_graph(value1, value2):
    total = value1 + value2
    percentage1 = (value1 / total) * 100
    percentage2 = (value2 / total) * 100

    canvas.delete("all")
    canvas.create_rectangle(0, 0, percentage1 * 5, 30, fill="blue")
    canvas.create_rectangle(percentage1 * 5, 0, percentage1 * 5 + percentage2 * 5, 30, fill="red")


root = tk.Tk()
root.title("Horizontal Bar Graph")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(frame, width= 700, height=40)
canvas.pack()

# Initial values for the two related items
value_item1 = 1
value_item2 = 99

create_bar_graph(value_item1, value_item2)

root.mainloop()
