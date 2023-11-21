from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from resources.Colors import Color as color

app = Tk()
app.title("Attendance Application")

app.iconbitmap('image.jpg')
app.geometry("1100x700")
app.resizable(width=False, height=False)
justOpened = False
app.config(background=color.white)
style = ttk.Style()

ssid = "attendance"
pw = "attendance"
style.configure("TEntry", bordercolor="")

backList = []

imageLeftHand = ImageTk.PhotoImage(Image.open('img/left.png'))
imageLeftChecked = ImageTk.PhotoImage(Image.open('img/leftChecked.png'))
imageRightHand = ImageTk.PhotoImage(Image.open('img/right.png'))
imageRightChecked = ImageTk.PhotoImage(Image.open('img/rightChecked.png'))
imageBackArrow = ImageTk.PhotoImage(Image.open('img/left-arrow.png'))

backBtn = Button(app, image=imageBackArrow, pady=10, padx=20, background=color.white, border=0)
backBtn.grid(sticky="nw")

# make the next button appear at the bottom
nextBtn = Button(app, text="Next", padx=20, pady=10, anchor="se")
# nextBtn.grid(sticky="es")

isOpened = Frame


# callerID = "001"























def clear_content():
    for widget in app.winfo_children():
        if widget == isOpened:
            widget.destroy()
    pass


def switch():
    clear_content()
    print(backList)
    try:
        backList.pop()
        if backList[-1] == "001":
            firstPage()
        elif backList[-1] == "002":
            loginPage()
        elif backList[-1] == "003":
            splashScreen()
        elif backList[-1] == "004":
            registerAdmin()
        elif backList[-1] == "005":
            adminPage1()
        elif backList[-1] == "006":
            adminPage2()
        elif backList[-1] == "007":
            addEmployeePage()
        elif backList[-1] == "008":
            addEmployeeNextPage()
        elif backList[-1] == "009":
            signingPage()
    except IndexError:
        print("Empty List")
        firstPage()


# firstPage()
backBtn.config(command=switch)
firstPage()

app.mainloop()
