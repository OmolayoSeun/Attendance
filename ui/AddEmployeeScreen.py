import time
from tkinter import ttk

import threading
from resources.Images import Images
from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from database.DB import DB

empDetails = []
returnResult1 = None
returnResult2 = None


def save():
    print(empDetails)
    DB.saveEmpInfo(empDetails[0], empDetails[1], empDetails[2], empDetails[3], empDetails[4], empDetails[5],
                   empDetails[6], str(returnResult1), str(returnResult2))
    pass


def __keepEmpDetails(frame, fName: str, mName: str, lName: str, phone: str, email: str, position: str):
    if fName == "Enter first name" or mName == "Enter middle name" or lName == "Enter last name" or \
            phone == "Enter phone no" or email == "Enter email" or position == "Enter position" or \
            fName == "" or mName == "" or lName == "" or phone == "" or email == "" or position == "":
        l = configLabel(Label(frame, text="Empty fields"))
        l.config(fg="red")
        l.grid(row=18, column=0, columnspan=3)

    else:
        global empDetails
        empDetails = [fName.capitalize() + phone, fName.capitalize(), mName.capitalize(), lName.capitalize(),
                      phone.capitalize(), email.capitalize(), position.capitalize()]
        addEmployeeNextPage()
    pass


def addEmployeePage():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewEmp

    configLabel(Label(frame, text="First Name: ", anchor='w')).grid(row=0, column=0, sticky="w")
    configLabel(Label(frame, text="Middle Name: ")).grid(row=3, column=0, sticky="w")
    configLabel(Label(frame, text="Last Name: ")).grid(row=6, column=0, sticky="w")
    configLabel(Label(frame, text="Phone No: ")).grid(row=9, column=0, sticky="w")
    configLabel(Label(frame, text="Email: ")).grid(row=12, column=0, sticky="w")
    configLabel(Label(frame, text="Position: ")).grid(row=15, column=0, sticky="w")

    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=2, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=5, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=8, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=11, column=1)
    Label(frame, font=('ariel', '5', 'normal'), bg=color.white).grid(row=14, column=1)

    firstName = ttk.Entry(frame, width=35)
    middleName = ttk.Entry(frame, width=35)
    lastName = ttk.Entry(frame, width=35)
    phone = ttk.Entry(frame, width=35)
    email = ttk.Entry(frame, width=35)
    position = ttk.Entry(frame, width=35)

    add_hint(firstName, "Enter first name")
    add_hint(middleName, "Enter middle name")
    add_hint(lastName, "Enter last name")
    add_hint(phone, "Enter phone no")
    add_hint(email, "Enter email")
    add_hint(position, "Enter position")

    btn = Button(frame, text="Next", padx=10,
                 command=lambda: __keepEmpDetails(frame, firstName.get(), middleName.get(), lastName.get(),
                                                  phone.get(), email.get(), position.get()))
    configButton(btn)

    firstName.grid(row=1, column=0, columnspan=3, ipady=5)
    middleName.grid(row=4, column=0, columnspan=3, ipady=5)
    lastName.grid(row=7, column=0, columnspan=3, ipady=5)
    phone.grid(row=10, column=0, columnspan=3, ipady=5)
    email.grid(row=13, column=0, columnspan=3, ipady=5)
    position.grid(row=16, column=0, columnspan=3, ipady=5)

    btn.grid(row=17, column=0, columnspan=3, pady=10, sticky='we')

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass


def addEmployeeNextPage():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewEmpNext

    text = configLabel(Label(frame, text="Put and remove right index finger on the sensor four times"))
    text.config(fg='red')

    left = configLabel(Label(frame, image=Images.imageLeftHand))
    right = configLabel(Label(frame, image=Images.imageRightTurn))

    text.grid(row=0, column=0, columnspan=3)
    left.grid(row=1, column=0)
    right.grid(row=1, column=2)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)

    from tools.Reader import Reader

    def getFingerPrint():
        global returnResult1
        global returnResult2

        while True:
            returnResult1 = Reader.getFingerPrint()
            if returnResult1 is None:
                text.config(text="Failed")
                time.sleep(2)
                text.config(text="Put and remove right index finger on the sensor four times")
            else:
                text.config(text="Right finger successful", fg='green')
                right.config(image=Images.imageRightChecked)
                time.sleep(2)
                break

        text.config(text="Put left index finger on the sensor", fg='red')
        left.config(image=Images.imageLeftTurn)

        while True:
            returnResult2 = Reader.getFingerPrint()
            if returnResult2 is None:
                text.config(text="Failed")
                time.sleep(2)
                text.config(text="Put and remove left index finger on the sensor four times")
            else:
                text.config(text="Left finger successful", fg='green')
                left.config(image=Images.imageLeftChecked)
                time.sleep(2)
                break

        save()
        text.config(text="Saved!")
        time.sleep(2)
        from ui.AdminScreen import adminPage1
        adminPage1()
        pass

    thread = threading.Thread(target=getFingerPrint)
    thread.start()
    pass
# TODO work on the fingerprint page
