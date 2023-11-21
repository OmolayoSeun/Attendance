from tkinter import *
from PIL import ImageTk, Image
import sqlite3

app = Tk()
app.title('Testing app')
app.geometry("400x400")

com = sqlite3.connect('database/data.db')

c = com.cursor()
#
# c.execute("""CREATE TABLE address(
#     firstName text,
#     lastName text,
#     phoneNo text,
#     email text
#     )""")

fName = Entry(app, width=30)
fName.grid(row=0, column=1, padx=20)

lName = Entry(app, width=30)
lName.grid(row=1, column=1, padx=20)

phoneNo = Entry(app, width=30)
phoneNo.grid(row=2, column=1, padx=20)

email = Entry(app, width=30)
email.grid(row=3, column=1, padx=20)

fL = Label(app, text="First Name: ")
fL.grid(row=0, column=0)

lL = Label(app, text="Last Name: ")
lL.grid(row=1, column=0)

ph = Label(app, text="Phone No: ")
ph.grid(row=2, column=0)

em = Label(app, text="Email: ")
em.grid(row=3, column=0)


def submit():
    pass


submitBtn = Button(app, text="save", command=submit)
submitBtn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

com.commit()
com.close()

app.mainloop()
