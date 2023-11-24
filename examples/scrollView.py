import tkinter as tk

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root = tk.Tk()
root.title("Scrollable Frame Example")

# Create a frame to hold the scrollable content
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas within the frame
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar for the canvas (vertical scrolling)
scrollbar = tk.Scrollbar(main_frame, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create another frame to hold the content inside the canvas
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Add some widgets (labels in this example) to the content frame
for i in range(50):
    label = tk.Label(content_frame, text=f"Label {i}")
    label.pack()

# Update the scrollable region
content_frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

root.mainloop()
