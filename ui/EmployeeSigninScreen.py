import threading
from tkinter import ttk

from database.DB import DB
from resources.Variables import Variables as v
from tools.ClearContent import clear_content
from tools.Configure import *
from tools.Reader import Reader
from datetime import datetime


fingPrints = None
viewDict = {}

# Gets the fingerprints from the database
def __getInfoFromDB():
    global fingPrints
    fingPrints = DB.getFingPrints()
    pass


# Display the signin interface
def signingPage():
    # for mouse wheel action
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    clear_content()
    frame = Frame(v.app)
    configFrame(frame)

    v.holdFrameReference = frame
    v.currentView = v.viewAttendance

    __getInfoFromDB()

    configLabel(Label(frame, text="Attendance", font=('ariel', '20'))).grid(row=0, column=2, columnspan=3, pady=10)

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

    treeview = ttk.Treeview(content_frame, height=13, columns=("First Name", "Last Name", "Date", "Sign-In Time",
                                                               "Sign-Out Time"), show="headings")

    treeview.column("#1", width=200)
    treeview.column("#2", width=200)
    treeview.column("#3", width=200)
    treeview.column("#4", width=200)
    treeview.column("#5", width=200)

    # Define the column headings
    treeview.heading("#1", text="First Name")
    treeview.heading("#2", text="Last Name")
    treeview.heading("#3", text="Date")
    treeview.heading("#4", text="Sign-In Time")
    treeview.heading("#5", text="Sign-In Time")

    # Pack the treeview widget into the main window
    treeview.pack()

    # Update the scrollable region
    content_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    if fingPrints is None or fingPrints == [[]]: \
            Label(frame, text="There's no registered employee!", font=('ariel', 12, 'bold'), fg='red', bg='white').grid(
                row=2, column=2, columnspan=3, sticky='we')

    v.app.update_idletasks()
    cenX = (v.app.winfo_width() - frame.winfo_reqwidth()) // 2
    cenY = ((v.app.winfo_height() - frame.winfo_reqheight()) // 2)

    frame.place(x=cenX, y=cenY)

    # this function is called in a thread to verify fingerprints
    def getFingerPrint():
        global fingPrints
        f = []
        for i in range(len(fingPrints)):
            f.append(fingPrints[i][1])
            f.append(fingPrints[i][2])
            print(f)

        while True:
            index = Reader.verifyFingerPrint(f)
            if index == "ERR100":
                print("ERR100")
            elif index == "ERR200":
                print("ERR100")
            elif index == "ERR300":
                print("ERR100")
            else:
                emp = DB.getEmpInfo(fingPrints[int(str(index))][0])
                if emp is not None and emp is not [[]]:
                    if viewDict.get(emp[0]) is not None:
                        # sign out
                        print("signout did not run")
                        listItem = viewDict[emp[0]]
                        if listItem[4] == "":
                            listItem[4] = datetime.now().strftime("%H:%M:%S")
                            viewDict[emp[0]] = listItem
                            DB.saveEmpAttendance(emp[0], listItem[2], listItem[3], listItem[4])

                    else:
                        # sign in
                        listItem = [emp[1], emp[3], datetime.now().strftime("%d-%m-%Y"),
                                    datetime.now().strftime("%H:%M:%S"), ""]
                        viewDict[emp[0]] = listItem
                        print(viewDict[emp[0]])
                        DB.saveEmpAttendance(emp[0], listItem[2], listItem[3], listItem[4])

                    items = treeview.get_children()
                    for item in items:
                        treeview.delete(item)

                    for key in viewDict.keys():
                        dictItem = viewDict[key]
                        treeview.insert("", 'end',
                                        values=(dictItem[0], dictItem[1], dictItem[2], dictItem[3], dictItem[4]))

    # Thread for calling the function that will listen for fingerprint data
    thread = threading.Thread(target=getFingerPrint)
    thread.start()
    pass
