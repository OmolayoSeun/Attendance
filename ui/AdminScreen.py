from tkinter import Label, Frame, ttk

from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from database.DB import DB



def __saveAdmin(compName: str, bizType: str, pwd: str, comPwd: str, notifyTop: Label, notify: Label):
    if compName == "" or bizType == "" or pwd == "" or comPwd == "":
        notifyTop.config(text="Empty Fields!", fg="red")
        return
    elif pwd != comPwd:
        notify.config(text="Password does not match!", fg="red")
        return
    else:
        from ui.LoginScreen import loginPage
        result = DB.saveAdminInfo(compName, bizType, pwd)
        if result:
            loginPage()
        else:
            notify.config(text="Can't create admin!", fg="red")
        # else will contain dialog for password does not match
    pass


def saveNewAdmin(name: str, biz: str, pwd: str):
    pass


# 004
def registerAdmin():
    clear_content()
    frame = Frame(v.app)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(1, weight=3)
    configFrame(frame)

    v.holdFrameReference = frame
    #backList.append("004")

    notifyTop = Label(frame, text="")
    Label(frame, text="Company Name: ").grid(row=1, column=0, sticky="w")
    Label(frame, text="Business Type: ").grid(row=2, column=0, sticky="w")
    notify = Label(frame, text="")
    Label(frame, text="Password: ").grid(row=4, column=0, sticky="w")
    Label(frame, text="Confirm Password: ").grid(row=5, column=0, sticky="w")

    compName = Entry(frame, width=35, borderwidth=5)
    bizType = Entry(frame, width=35, borderwidth=5)
    pwd = Entry(frame, width=35, borderwidth=5)
    comPwd = Entry(frame, width=35, borderwidth=5)

    # btn1 = Button(app, text="Back", padx=40, pady=20, command=firstPage)
    btn2 = Button(frame, text="Register", padx=40,
                  command=lambda: __saveAdmin(compName.get(), bizType.get(),
                                              pwd.get(), comPwd.get(), notifyTop, notify))

    notifyTop.grid(row=0, column=1)
    notify.grid(row=3, column=1)
    compName.grid(row=1, column=1, columnspan=2)
    bizType.grid(row=2, column=1, columnspan=2)
    pwd.grid(row=4, column=1, columnspan=2)
    comPwd.grid(row=5, column=1, columnspan=2)
    # btn1.grid(row=2, column=0)
    btn2.grid(row=6, column=1)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)


# 005
def adminPage1():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    #backList.append("005")

    Label(frame, text="Company Name").grid(row=0, column=0)
    Label(frame, text="Business Type").grid(row=0, column=1)

    # Create the treeview widget
    treeview = ttk.Treeview(frame, columns=("First Name", "Middle Name", "Last Name", "Phone No.", "Email", "Position"), show="headings")

    # Define the column headings
    treeview.heading("First Name", text="First Name")
    treeview.heading("Middle Name", text="Middle Name")
    treeview.heading("Last Name", text="Last Name")
    treeview.heading("Phone No", text="Phone No")
    treeview.heading("Email", text="Email")
    treeview.heading("Position", text="Position")

    # Add items to the treeview
    result = DB.getEmpList()
    for r in result:
        treeview.insert("", 'end', '1', values=(r[1], r[2], r[3], r[4], r[5], r[6]))

    # Pack the treeview widget into the main window
    treeview.pack(fill='both', expand=True)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


# 006
def adminPage2():
    pass





