from resources.Images import Images
from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from database.DB import DB

empDetails = []


def save():
    DB.saveEmpInfo(empDetails[0], empDetails[0], empDetails[1], empDetails[2], empDetails[3], empDetails[4],
                   empDetails[5])
    pass


def __keepEmpDetails(fName: str, mName: str, lName: str, phone: str, email: str, position: str):
    empDetails.append(fName)
    empDetails.append(mName)
    empDetails.append(lName)
    empDetails.append(phone)
    empDetails.append(email)
    empDetails.append(position)

    addEmployeeNextPage()
    pass


# 007
def addEmployeePage():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    # backList.append("007")

    configLabel(Label(frame, text="First Name: ")).grid(row=0, column=0, sticky="w")
    configLabel(Label(frame, text="Middle Name: ")).grid(row=1, column=0, sticky="w")
    configLabel(Label(frame, text="Last Name: ")).grid(row=2, column=0, sticky="w")
    configLabel(Label(frame, text="Phone No: ")).grid(row=3, column=0, sticky="w")
    configLabel(Label(frame, text="Email: ")).grid(row=4, column=0, sticky="w")
    configLabel(Label(frame, text="Position: ")).grid(row=5, column=0, sticky="w")

    firstName = (Entry(frame, width=35, borderwidth=5))
    middleName = Entry(frame, width=35, borderwidth=5)
    lastName = Entry(frame, width=35, borderwidth=5)
    phone = Entry(frame, width=35, borderwidth=5)
    email = Entry(frame, width=35, borderwidth=5)
    position = Entry(frame, width=35, borderwidth=5)

    btn = Button(frame, text="Next", padx=10,
                 command=lambda: __keepEmpDetails(firstName.get(), middleName.get(), lastName.get(),
                                                  phone.get(), email.get(), position.get()))
    configEntry(firstName)
    configEntry(middleName)
    configEntry(lastName)
    configEntry(phone)
    configEntry(email)
    configEntry(position)
    configButton(btn)

    firstName.grid(row=0, column=1, columnspan=3, pady=5)
    middleName.grid(row=1, column=1, columnspan=3)
    lastName.grid(row=2, column=1, columnspan=3, pady=5)
    phone.grid(row=3, column=1, columnspan=3)
    email.grid(row=4, column=1, columnspan=3, pady=5)
    position.grid(row=5, column=1, columnspan=3)
    # btn1.pack()
    btn.grid(row=6, column=2, pady=5)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


# 008
def addEmployeeNextPage():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    # backList.append("008")

    text = configLabel(Label(frame, text="Put Right index Finger on the sensor", fg="red"))
    left = configLabel(Label(frame, image=Images.imageLeftHand))
    right = configLabel(Label(frame, image=Images.imageRightHand))
    btn1 = Button(frame, text="Save", padx=10, command=save)
    configButton(btn1)
    # frame.config(image=image1)

    text.grid(row=0, column=0, columnspan=3)
    left.grid(row=1, column=0)
    right.grid(row=1, column=2)
    btn1.grid(row=2, column=1)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass
