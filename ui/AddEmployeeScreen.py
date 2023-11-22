from resources.Images import Images
from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *


def __saveEmployee():
    pass


# 007
def addEmployeePage():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    #backList.append("007")

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
    #backList.append("008")

    text = Label(frame, text="Put Right index Finger on the sensor", fg="red")
    left = Label(frame, image=Images.imageLeftHand)
    right = Label(frame, image=Images.imageRightHand)

    # frame.config(image=image1)

    text.grid(row=0, column=0, columnspan=3)
    left.grid(row=1, column=0)
    right.grid(row=1, column=2)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)
    pass
