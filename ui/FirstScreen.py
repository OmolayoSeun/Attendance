from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from ui.EmployeeSigninScreen import signingPage
from ui.LoginScreen import loginPage


def button_click(call):
    if call == "Signing":
        signingPage()
    elif call == "Admin":
        loginPage()


def firstPage():
    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame

    v.app.update_idletasks()
    btn1 = Button(frame, text="Signing Page", width=20, border=0, cursor='hand2',
                  font=('Ariel', 12, 'bold'), padx=30, pady=10,command=lambda: button_click("Signing"))

    btn2 = Button(frame, text="Admin Page",width=20, border=0, cursor='hand2',
                  font=('Ariel', 12, 'bold'), padx=30, pady=10,command=lambda: button_click("Admin"))

    configLabel(Label(frame, pady=10)).grid(row=1)
    configButton(btn1)
    configButton(btn2)

    btn1.grid(row=0, column=0)
    btn2.grid(row=2, column=0)

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)

