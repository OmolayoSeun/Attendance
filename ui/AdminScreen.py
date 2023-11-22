from tkinter import Label, Frame, ttk

from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from database.DB import DB
from ui.AddEmployeeScreen import addEmployeePage


adminInfo = []
empInfo = []


def __getInfoFromDB():
    global adminInfo
    global empInfo
    adminInfo = DB.getAdminInfo()
    empInfo = DB.getEmpList()

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


# 004
def registerAdmin():
    clear_content()
    frame = Frame(v.app)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(1, weight=3)
    configFrame(frame)

    v.holdFrameReference = frame
    # backList.append("004")

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
    # backList.append("005")
    __getInfoFromDB()
    configLabel(Label(frame, text=f"Company Name: {adminInfo[1]}")).grid(row=0, column=0, pady=10)
    configLabel(Label(frame, text=f"Business Type: {adminInfo[2]}")).grid(row=0, column=1)

    # Create the treeview widget
    treeview = ttk.Treeview(frame, columns=("First Name", "Middle Name", "Last Name", "Phone No.", "Email", "Position"),
                            show="headings")

    treeview.column("#1", width=150)
    treeview.column("#2", width=150)
    treeview.column("#3", width=150)
    treeview.column("#4", width=150)
    treeview.column("#5", width=150)
    treeview.column("#6", width=150)

    # Define the column headings
    treeview.heading("#1", text="First Name")
    treeview.heading("#2", text="Middle Name")
    treeview.heading("#3", text="Last Name")
    treeview.heading("#4", text="Phone No")
    treeview.heading("#5", text="Email")
    treeview.heading("#6", text="Position")

    # Add items to the treeview
    result = DB.getEmpList()

    if empInfo is not None:
        print(empInfo)
        for r in empInfo:
            treeview.insert("", 'end', values=(r[1], r[2], r[3], r[4], r[5], r[6]))

    # Pack the treeview widget into the main window
    treeview.grid(row=1, column=0, columnspan=7)

    configDefBtn(Button(frame, text="Add Employee", padx=10, command=lambda: addEmployeePage())).grid(row=2, column=6, pady=5)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


# 006
def adminPage2():
    pass
