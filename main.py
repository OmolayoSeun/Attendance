from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from Colors import Color as color

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


def __saveEmployee():
    pass


def __saveAdmin(compName: str, bizType: str, pwd: str, comPwd: str, notifyTop: Label, notify: Label):
    if compName == "" or bizType == "" or pwd == "" or comPwd == "":
        notifyTop.config(text="Empty Fields!", fg="red")
        return
    elif pwd != comPwd:
        notify.config(text="Password does not match!", fg="red")
        return
    else:
        saveNewAdmin(compName, bizType, pwd)
        loginPage()
        # else will contain dialog for password does not match
    pass


def saveNewAdmin(name: str, biz: str, pwd: str):
    pass


def button_click(call):
    if call == "Signing":
        signingPage()
    elif call == "Admin":
        loginPage()


def __nextLogin(e1: Entry, e2: Entry, frame):
    username = e1.get()
    password = e2.get()
    # ssid = None
    print(username)
    if username == ssid and password == pw:
        adminPage1()
    elif ssid is None:
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


def configFrame(frame: Frame):
    frame.config(
        background=color.white
    )
    pass


def configLabel(item: Label):
    item.config(
        background=color.white
    )
    return item


def configEntry(item: Entry):
    item.config(border=0, background=color.white)
    pass



def configButton(item: Button):
    item.config(
        background=color.skyBlue, foreground=color.white,
        activebackground=color.green, activeforeground=color.white,
        highlightthickness=2, highlightbackground=color.green, highlightcolor=color.skyBlue,
    )
    pass


# 001
def firstPage():
    clear_content()
    frame = Frame(app)
    configFrame(frame)

    global isOpened
    isOpened = frame
    backList.append("001")

    app.update_idletasks()
    btn1 = Button(frame, text="Signing Page", width=20, border=0, cursor='hand2',
                  font=('Ariel', 12, 'bold'), padx=30, pady=10,command=lambda: button_click("Signing"))

    btn2 = Button(frame, text="Admin Page",width=20, border=0, cursor='hand2',
                  font=('Ariel', 12, 'bold'), padx=30, pady=10,command=loginPage)

    configLabel(Label(frame, pady=10)).grid(row=1)
    configButton(btn1)
    configButton(btn2)

    btn1.grid(row=0, column=0)
    btn2.grid(row=2, column=0)

    app.update_idletasks()
    cenX = (app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)


# 002
def loginPage():
    clear_content()
    frame = Frame(app)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(1, weight=0)
    configFrame(frame)

    global isOpened
    isOpened = frame
    backList.append("002")

    Label(frame, text="Company Name: ").grid(row=0, column=0, sticky="w")
    Label(frame, text="Company password: ").grid(row=1, column=0, sticky="w")
    compName = ttk.Entry(frame, width=35)
    compPassword = ttk.Entry(frame, width=35)

    btn1 = Button(frame, text="Register", padx=10, command=registerAdmin)
    btn2 = Button(frame, text="Login", padx=10, command=lambda: __nextLogin(compName, compPassword, frame))

    btn1.grid(row=2, column=1)
    btn2.grid(row=2, column=2)

    compName.grid(row=0, column=1, columnspan=2)
    compPassword.grid(row=1, column=1, columnspan=2)

    app.update_idletasks()
    cenX = (app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)


# 003
def splashScreen():
    pass


# 004
def registerAdmin():
    clear_content()
    frame = Frame(app)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(1, weight=3)
    configFrame(frame)

    global isOpened
    isOpened = frame
    backList.append("004")

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

    app.update_idletasks()
    cenX = (app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)


# 005
def adminPage1():
    clear_content()
    frame = Frame(app)
    configFrame(frame)

    global isOpened
    isOpened = frame
    backList.append("005")

    Label(frame, text="Company Name").grid(row=0, column=0)
    Label(frame, text="Business Type").grid(row=0, column=1)

    app.update_idletasks()
    cenX = (app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


# 006
def adminPage2():
    pass


# 007
def addEmployeePage():
    clear_content()
    frame = Frame(app)
    configFrame(frame)

    global isOpened
    isOpened = frame
    backList.append("007")

    Label(frame, text="First Name: ").grid(row=0, column=0, sticky="w")
    Label(frame, text="Middle Name: ").grid(row=1, column=0, sticky="w")
    Label(frame, text="Last Name: ").grid(row=2, column=0, sticky="w")
    Label(frame, text="Phone No: ").grid(row=3, column=0, sticky="w")
    Label(frame, text="Email: ").grid(row=4, column=0, sticky="w")
    Label(frame, text="Position: ").grid(row=5, column=0, sticky="w")

    firstName = Entry(frame, width=35, borderwidth=5)
    middleName = Entry(frame, width=35, borderwidth=5)
    lastName = Entry(frame, width=35, borderwidth=5)
    phone = Entry(frame, width=35, borderwidth=5)
    email = Entry(frame, width=35, borderwidth=5)
    position = Entry(frame, width=35, borderwidth=5)

    # btn1 = Button(app, text="Back", padx=40, pady=20, command=firstPage)
    btn2 = Button(frame, text="Next", padx=10, command=lambda: __saveEmployee())

    firstName.grid(row=0, column=1, columnspan=3)
    middleName.grid(row=1, column=1, columnspan=3)
    lastName.grid(row=2, column=1, columnspan=3)
    phone.grid(row=3, column=1, columnspan=3)
    email.grid(row=4, column=1, columnspan=3)
    position.grid(row=5, column=1, columnspan=3)
    # btn1.pack()
    btn2.grid(row=6, column=2)

    app.update_idletasks()
    cenX = (app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


# 008
def addEmployeeNextPage():
    clear_content()
    frame = Frame(app)
    configFrame(frame)

    global isOpened
    isOpened = frame
    backList.append("008")

    text = Label(frame, text="Put Right index Finger on the sensor", fg="red")
    left = Label(frame, image=imageLeftHand)
    right = Label(frame, image=imageRightHand)

    # frame.config(image=image1)

    text.grid(row=0, column=0, columnspan=3)
    left.grid(row=1, column=0)
    right.grid(row=1, column=2)

    app.update_idletasks()
    cenX = (app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


# 009
def signingPage():
    pass


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
