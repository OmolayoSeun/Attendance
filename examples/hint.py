import tkinter as tk

def on_entry_click(event):
    if entry.get() == 'Enter your text here':
        entry.delete(0, tk.END)
        entry.config(fg='black')  # Change text color to black

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your text here')
        entry.config(fg='grey')  # Change text color to grey

root = tk.Tk()
root.title("Entry with Hint")

# Create the Entry widget
entry = tk.Entry(root, fg='grey')  # Set default text color to grey
entry.insert(0, 'Enter your text here')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(padx=10, pady=10)

root.mainloop()
