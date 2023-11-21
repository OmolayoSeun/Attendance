
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
