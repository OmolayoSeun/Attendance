import tkinter
from tkinter import ttk

from database.DB import DB
from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from ui.AddEmployeeScreen import addEmployeePage

adminInfo = []
empInfo = []


def __getInfoFromDB():
    global adminInfo
    global empInfo
    adminInfo = DB.getAdminInfo()
    empInfo = DB.getEmpList()


def __saveAdmin(hospitalName: str, pwd: str, comPwd: str, notifyTop: Label, notify: Label):
    if hospitalName == "Enter name" \
            or pwd == "Enter password" or comPwd == "Confirm password" \
            or hospitalName == "" or pwd == "" or comPwd == "":
        notifyTop.config(text="Empty Fields!", fg="red")
        return
    elif pwd != comPwd:
        notify.config(text="Password does not match!", fg="red")
        return
    else:
        from ui.LoginScreen import loginPage
        result = DB.saveAdminInfo(hospitalName, pwd)
        if result:
            loginPage()
        else:
            notify.config(text="Can't create admin!", fg="red")
        # else will contain dialog for password does not match
    pass


def deleteUser(index: int):
    result = DB.removeEmp(empInfo[index][0])
    if result:
        #alert dialog
        adminPage1()
    else:
        #alert dialog
        print("An error occured")
    pass


def registerAdmin():
    clear_content()
    frame = Frame(v.app)
    frame.columnconfigure(0, weight=0)
    frame.columnconfigure(1, weight=3)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewRegister

    notifyTop = configLabel(Label(frame, text=""))
    configLabel(Label(frame, text="Hospital Name: ")).grid(row=1, column=0, sticky="w")
    Label(frame, text="", font=('ariel', '1'), bg=color.white).grid(row=3, column=0)
    Label(frame, text="", font=('ariel', '1'), bg=color.white).grid(row=8, column=0)
    notify = configLabel(Label(frame, text=""))
    configLabel(Label(frame, text="Password: ")).grid(row=6, column=0, sticky="w")
    configLabel(Label(frame, text="Confirm Password: ")).grid(row=9, column=0, sticky="w")

    compName = ttk.Entry(frame, width=35)
    pwd = ttk.Entry(frame, width=35)
    comPwd = ttk.Entry(frame, width=35)

    add_hint(compName, "Hospital Name")
    add_hint(pwd, "Password")
    add_hint(comPwd, "Confirm password")

    btn = Button(frame, text="Register", padx=40,
                 command=lambda: __saveAdmin(compName.get(),
                                             pwd.get(), comPwd.get(), notifyTop, notify))
    configButton(btn)

    notifyTop.grid(row=0, column=0)
    notify.grid(row=5, column=0)
    compName.grid(row=2, column=0, ipady=5)
    pwd.grid(row=7, column=0, ipady=5)
    comPwd.grid(row=10, column=0, ipady=5)
    btn.grid(row=11, column=0, pady=5)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)


def adminPage1():
    def on_treeview_click(event):
        row_id = treeview.identify_row(event.y)  # Get the ID of the clicked row
        index = treeview.index(row_id)  # Get the index of the clicked row
        print(f"You clicked on row index: {index}")
        adminPage2(index)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewAdmin1

    __getInfoFromDB()

    configLabel(Label(frame, text="Records")).grid(row=0, column=3, columnspan=2, pady=10)

    # Create the treeview widget
    canvas = tk.Canvas(frame, background=color.white, width=1000)
    canvas.grid(row=1, column=0, columnspan=7)

    # Add a scrollbar for the canvas (vertical scrolling)
    scrollbar = tk.Scrollbar(frame, command=canvas.yview, background=color.white)
    scrollbar.grid(row=1, column=6, sticky='nse')

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Create another frame to hold the content inside the canvas
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    treeview = ttk.Treeview(content_frame, height=13,
                            columns=("First Name", "Middle Name", "Last Name", "Phone No.", "Email", "Position"),
                            show="headings")

    treeview.column("#1", width=166)
    treeview.column("#2", width=167)
    treeview.column("#3", width=167)
    treeview.column("#4", width=168)
    treeview.column("#5", width=167)
    treeview.column("#6", width=167)

    # Define the column headings
    treeview.heading("#1", text="First Name")
    treeview.heading("#2", text="Middle Name")
    treeview.heading("#3", text="Last Name")
    treeview.heading("#4", text="Phone No")
    treeview.heading("#5", text="Email")
    treeview.heading("#6", text="Position")

    if empInfo is not None and empInfo != [[]]:
        print(empInfo)
        for r in empInfo:
            treeview.insert("", 'end', values=(r[1], r[2], r[3], r[4], r[5], r[6]))
        treeview.bind("<ButtonRelease-1>", on_treeview_click)

    # Pack the treeview widget into the main window
    treeview.pack()

    # Update the scrollable region
    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    configDefBtn(Button(frame, text="Add +", command=lambda: addEmployeePage())).grid(row=2, column=6,
                                                                                      pady=5, sticky='we')

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


def adminPage2(index: int):
    # __getInfoFromDB()

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_bar_graph(canvasObj: tkinter.Canvas, value1, value2, value3):
        size = 9
        total = value1 + value2 + value3
        if total == 0:
            value3 = 100
            total = 100
        percentage1 = (value1 / total) * 100
        percentage2 = (value2 / total) * 100
        percentage3 = (value3 / total) * 100

        canvasObj.delete("all")
        canvasObj.create_rectangle(0, 0, percentage1 * size, 30, fill=color.green)
        canvasObj.create_rectangle(percentage1 * size, 0, (percentage1 * size) + (percentage2 * size), 30, fill="red")
        canvasObj.create_rectangle((percentage1 * size) + (percentage2 * size), 0,
                                   (percentage1 * size) + (percentage2 * size) + (percentage3 * size), 30, fill="grey")

    def enter(event=None):
        # barGraph1.close()
        x, y, cx, cy = barGraph1.bbox("insert")
        x += barGraph1.winfo_rootx() + 25
        y += barGraph1.winfo_rooty() + 20
        barGraph1.tw = tk.Toplevel(barGraph1)
        barGraph1.tw.wm_overrideredirect(True)
        barGraph1.tw.wm_geometry("+%d+%d" % (x, y))
        popText = tk.Label(barGraph1.tw, text="hello", justify='left',
                           background="#ffffff", relief='solid', borderwidth=1,
                           font=("times", "8", "normal"))
        popText.pack(ipadx=1)

    def close(event=None):
        if barGraph1.tw:
            barGraph1.tw.destroy()

    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewAdmin2

    frame.columnconfigure(0, weight=5)
    frame.columnconfigure(1, weight=10)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)

    configLabel(Label(frame, text=f"First Name: {empInfo[index][1]}", width=58, anchor='w')).grid(row=0, column=0,
                                                                                                  columnspan=2,
                                                                                                  sticky='we')
    configLabel(Label(frame, text=f"Middle Name: {empInfo[index][2]}")).grid(row=1, column=0, columnspan=2, sticky='w')
    configLabel(Label(frame, text=f"Last Name: {empInfo[index][3]}")).grid(row=2, column=0, columnspan=2, sticky='w')
    configLabel(Label(frame, text=f"Phone: {empInfo[index][4]}", width=58, anchor='w')).grid(row=0, column=2,
                                                                                             columnspan=2, sticky='w')
    configLabel(Label(frame, text=f"Email: {empInfo[index][5]}")).grid(row=1, column=2, columnspan=2, sticky='w')
    configLabel(Label(frame, text=f"Position: {empInfo[index][6]}")).grid(row=2, column=2, columnspan=2, sticky='w')
    # configLabel(Label(frame, text=f"Gender: {empInfo[index][6]}")).grid(row=3, column=0, columnspan=2, sticky='w')

    configLabel(Label(frame, text="    ")).grid(row=10, column=3, pady=10)  # dummy label
    delete = Button(frame, text="Delete", command=lambda: deleteUser(index))
    configDeleteBtn(delete)
    delete.grid(row=10, column=3, rowspan=1, pady=5, ipadx=10, sticky='e')

    Label(frame, text="Day", fg=color.white, bg=color.skyBlue, borderwidth=1, relief='solid',
          font=('ariel', '10', 'bold')) \
        .grid(row=4, column=0, sticky='we')
    Label(frame, text="Date", fg=color.white, bg=color.skyBlue, border=1, relief='solid', font=('ariel', '10', 'bold')) \
        .grid(row=4, column=1, sticky='we')
    Label(frame, text="Sign-in Time", fg=color.white, bg=color.skyBlue, border=1, relief='solid',
          font=('ariel', '10', 'bold')) \
        .grid(row=4, column=2, sticky='we')
    Label(frame, text="Sign-out Time", fg=color.white, bg=color.skyBlue, border=1, relief='solid',
          font=('ariel', '10', 'bold')) \
        .grid(row=4, column=3, sticky='we')

    canvas = tk.Canvas(frame, background=color.white)
    canvas.grid(row=5, column=0, columnspan=4, sticky='we')
    # Add a scrollbar for the canvas (vertical scrolling)
    scrollbar = tk.Scrollbar(frame, command=canvas.yview, background=color.white)
    scrollbar.grid(row=5, column=3, sticky='nse')

    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind_all("<MouseWheel>", on_mousewheel)

    # Create another frame to hold the content inside the canvas
    content_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Add some widgets (labels in this example) to the content frame
    # for i in range(50):
    #     label = tk.Label(content_frame, text=f"Label {i}")
    #     label.pack()
    # TODO fill the scroll bar with history of the user
    label = tk.Label(content_frame, text=f"Label ", height=130)
    label.pack()

    # Update the scrollable region
    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    configLabel(Label(frame, text="Sign-In Stat")).grid(row=6, column=0, pady=5)
    barGraph1 = tk.Canvas(frame, width=898, height=25, bg=color.white, borderwidth=0)

    barGraph1.bind("<Enter>", enter)
    barGraph1.bind("<Leave>", close)
    barGraph1.id = None
    barGraph1.tw = None

    barGraph1.grid(row=7, column=0, columnspan=4)
    create_bar_graph(barGraph1, 10, 17, 2)

    configLabel(Label(frame, text="Sign-Out Stat")).grid(row=8, column=0, pady=5)
    barGraph2 = tk.Canvas(frame, width=898, height=25, bg=color.white, borderwidth=0)
    barGraph2.grid(row=9, column=0, columnspan=4)
    create_bar_graph(barGraph2, 1, 0, 2)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass
