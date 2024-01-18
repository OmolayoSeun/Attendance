from tkinter import *
from tkinter import ttk

from resources.Colors import Color as color
from resources.Images import *
from resources.Variables import Variables as v
from ui.AddEmployeeScreen import addEmployeePage, addEmployeeNextPage
from ui.AdminScreen import adminPage1, registerAdmin, adminPage2
from ui.FirstScreen import firstPage
from ui.LoginScreen import loginPage

v.app = Tk()
v.app.title("Attendance Application")

# v.app.iconbitmap('image.jpg')
v.app.geometry("1100x700")
v.app.resizable(width=False, height=False)
justOpened = False
v.app.config(background=color.white)
style = ttk.Style()

ssid = "attendance"
pw = "attendance"
style.configure("TEntry", bordercolor="")

backList = []

Images.imageLeftHand = ImageTk.PhotoImage(Image.open('img/left.png'))
Images.imageLeftChecked = ImageTk.PhotoImage(Image.open('img/leftChecked.png'))
Images.imageRightHand = ImageTk.PhotoImage(Image.open('img/right.png'))
Images.imageRightChecked = ImageTk.PhotoImage(Image.open('img/rightChecked.png'))
Images.imageBackArrow = ImageTk.PhotoImage(Image.open('img/left-arrow.png'))
Images.imageRightTurn = ImageTk.PhotoImage(Image.open('img/rightTurn.png'))
Images.imageLeftTurn = ImageTk.PhotoImage(Image.open('img/leftTurn.png'))

backBtn = Button(v.app, image=Images.imageBackArrow, pady=10, padx=20, background=color.white, border=0)
backBtn.grid(sticky="nw")


def back():
    print(v.currentView)
    if v.currentView == v.viewLogin:
        firstPage()
    elif v.currentView == v.viewAdmin1:
        loginPage()
    elif v.currentView == v.viewAdmin2:
        adminPage1()
    elif v.currentView == v.viewEmp:
        adminPage1()
    elif v.currentView == v.viewEmpNext:
        addEmployeePage()
    elif v.currentView == v.viewRegister:
        loginPage()
    pass


backBtn.config(command=back)


firstPage()
v.app.mainloop()


