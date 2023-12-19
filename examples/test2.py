import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry with Black Border")

# Create a Style object
style = ttk.Style()

# Set the border color for the "TEntry" class to an empty string (default)
style.configure("TEntry", bordercolor="")

# Create an Entry widget
entry = ttk.Entry(root)
entry.pack(padx=10, pady=10)

# Bind mouse enter and leave events to the entry widget
#entry.bind("<Enter>", add_border)
#entry.bind("<Leave>", remove_border)

root.mainloop()
#device_name = "9DFBF72D-0711-4D3A-9C2D-57B73A5E5F50"