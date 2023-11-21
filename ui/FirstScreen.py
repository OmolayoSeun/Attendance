
def button_click(call):
    if call == "Signing":
        signingPage()
    elif call == "Admin":
        loginPage()


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