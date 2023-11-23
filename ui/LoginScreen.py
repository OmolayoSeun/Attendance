from tkinter import ttk

from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from ui.AdminScreen import adminPage1, registerAdmin
from database.DB import DB


def __nextLogin(e1: Entry, e2: Entry, frame):
    username = e1.get()
    password = e2.get()

    adminInfo = DB.getAdminInfo()

    # ssid = None
    print(username)
    if username == adminInfo[1] and password == adminInfo[-1]:
        adminPage1()
    elif adminInfo[1] is None:
        txt = Label(frame, text="User does not exit")
        txt.config(fg="red")
        txt.grid(row=3, column=1)
    elif username == "" or password == "":
        txt = Label(frame, text="Empty Fields")
        txt.config(fg="red")
        txt.grid(row=3, column=1)
    else:
        txt = Label(frame, text="Invalid Password!")
        txt.config(fg="red")
        txt.grid(row=3, column=1)

    # should trow an error dialog

    pass


def loginPage():
    clear_content()
    frame = Frame(v.app)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(1, weight=0)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewLogin

    configLabel(Label(frame, text="Company Name: ")).grid(row=0, column=0, sticky="w")
    configLabel(Label(frame, text="Company password: ")).grid(row=2, column=0, sticky="w")
    compName = ttk.Entry(frame, font=('ariel', '20', 'normal'))
    compPassword = ttk.Entry(frame, font=('ariel', '20', 'normal'))

    add_hint(compName, "Enter Company Name")
    add_hint(compPassword, "Enter Company Password")

    btn1 = configDefBtn(Button(frame, text="Register", padx=10, command=registerAdmin))
    btn2 = configDefBtn(Button(frame, text="Login", padx=10, command=lambda: __nextLogin(compName, compPassword, frame)))

    btn1.grid(row=4, column=0)
    btn2.grid(row=4, column=1)

    compName.grid(row=1, column=0, columnspan=2, pady=5)
    compPassword.grid(row=3, column=0, columnspan=2, pady=5)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
