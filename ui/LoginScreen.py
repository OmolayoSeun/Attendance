
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
