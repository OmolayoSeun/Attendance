from tkinter import ttk

from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from ui.AdminScreen import adminPage1, registerAdmin
from database.DB import DB

# This function confirms the details and calls the admin page if the details matches
def __nextLogin(e1: Entry, e2: Entry, frame):
    username = e1.get()
    password = e2.get()

    adminInfo = DB.getAdminInfo()

    print(username)
    if username == adminInfo[1] and password == adminInfo[-1]:
        adminPage1()
    elif adminInfo[1] is None:
        txt = configLabel(Label(frame, text="User does not exit"))
        txt.config(fg="red")
        txt.grid(row=5, column=1)
    elif username == "" or password == "" or username == "Enter Company Name" or password == "Enter Company Password":
        txt = configLabel(Label(frame, text="Empty Fields"))
        txt.config(fg="red")
        txt.grid(row=5, column=1)
    else:
        txt = configLabel(Label(frame, text="Invalid Password!"))
        txt.config(fg="red")
        txt.grid(row=5, column=1)

    # should trow an error dialog

    pass

# This function displays the login page
def loginPage():
    clear_content()
    frame = Frame(v.app)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    configFrame(frame)


    style = ttk.Style()
    # Configure the style for the Entry widget
    style.configure('Custom.TEntry', foreground='blue', font=('Arial', 120))
    style.map('Custom.TEntry',
              fieldbackground=[('focus', 'yellow'), ('!focus', 'white')],
              foreground=[('disabled', 'grey')])

    v.holdFrameReference = frame
    v.currentView = v.viewLogin

    configLabel(Label(frame, text="Hospital Name: ", font=('ariel', '12', "normal"), foreground="grey")).grid(row=0, column=0, columnspan=3, sticky="w")
    configLabel(Label(frame, text="Password: ", font=('ariel', '12', "normal"), foreground="grey", pady=5)).grid(row=2, column=0,  columnspan=3, sticky="w")
    compName = ttk.Entry(frame,  width=35)
    compPassword = ttk.Entry(frame, width=35)

    add_hint(compName, "Hospital Name")
    add_hint(compPassword, "Password")

    btn1 = configDefBtn(Button(frame, text="Register", command=registerAdmin))
    btn2 = configDefBtn(Button(frame, text="Login", padx=10, command=lambda: __nextLogin(compName, compPassword, frame)))

    configButton(btn1)
    configButton(btn2)

    btn1.grid(row=4, column=0, pady=5, sticky="nswe")
    btn2.grid(row=4, column=2, pady=5, sticky="nswe")

    compName.grid(row=1, column=0, columnspan=3, pady=5, ipady=5)
    compPassword.grid(row=3, column=0, columnspan=3, pady=0, ipady=5)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
