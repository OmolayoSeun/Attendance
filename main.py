from tkinter import *
from tkinter import ttk
from resources.Colors import Color as color
from resources.Images import *
from resources.Variables import Variables as v
from ui.AddEmployeeScreen import addEmployeePage
from ui.AdminScreen import adminPage1
from ui.FirstScreen import firstPage
from ui.LoginScreen import loginPage

v.app = Tk()
v.app.title("Attendance Application")

v.app.geometry("1100x700")
v.app.resizable(width=False, height=False)
justOpened = False
v.app.config(background=color.white)
style = ttk.Style()

style.configure("TEntry", bordercolor="")


# initialising the images
Images.imageLeftHand = ImageTk.PhotoImage(Image.open('img/left.png'))
Images.imageLeftChecked = ImageTk.PhotoImage(Image.open('img/leftChecked.png'))
Images.imageRightHand = ImageTk.PhotoImage(Image.open('img/right.png'))
Images.imageRightChecked = ImageTk.PhotoImage(Image.open('img/rightChecked.png'))
Images.imageBackArrow = ImageTk.PhotoImage(Image.open('img/left-arrow.png'))
Images.imageRightTurn = ImageTk.PhotoImage(Image.open('img/rightTurn.png'))
Images.imageLeftTurn = ImageTk.PhotoImage(Image.open('img/leftTurn.png'))

# creating the back button
backBtn = Button(v.app, image=Images.imageBackArrow, pady=10, padx=20, background=color.white, border=0)
backBtn.grid(sticky="nw")


# function for the back arrow button
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
    elif v.currentView == v.viewAttendance:
        firstPage()
    pass

backBtn.config(command=back)

# calling the first interface
firstPage()

v.app.mainloop()
