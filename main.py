from tkinter import *
from tkinter import ttk
from resources.Variables import Variables as v
from  resources.Images import Image

from PIL import ImageTk, Image
from resources.Colors import Color as color
from resources.Images import *
from ui.FirstScreen import firstPage

v.app = Tk()
v.app.title("Attendance Application")

#v.app.iconbitmap('image.jpg')
v.app.geometry("1100x700")
v.app.resizable(width=False, height=False)
justOpened = False
v.app.config(background=color.white)
style = ttk.Style()

ssid = "attendance"
pw = "attendance"
style.configure("TEntry", bordercolor="")

backList = []

Images.imageLeftHand = ImageTk.PhotoImage(Image.open('img/left.png'))
Images.imageLeftChecked = ImageTk.PhotoImage(Image.open('img/leftChecked.png'))
Images.imageRightHand = ImageTk.PhotoImage(Image.open('img/right.png'))
Images.imageRightChecked = ImageTk.PhotoImage(Image.open('img/rightChecked.png'))
Images.imageBackArrow = ImageTk.PhotoImage(Image.open('img/left-arrow.png'))

backBtn = Button(v.app, image=Images.imageBackArrow, pady=10, padx=20, background=color.white, border=0)
backBtn.grid(sticky="nw")

# make the next button appear at the bottom
nextBtn = Button(v.app, text="Next", padx=20, pady=10, anchor="se")
# nextBtn.grid(sticky="es")

isOpened = Frame


# callerID = "001"







#
# def switch():
#     clear_content()
#     print(backList)
#     try:
#         backList.pop()
#         if backList[-1] == "001":
#             firstPage()
#         elif backList[-1] == "002":
#             loginPage()
#         elif backList[-1] == "003":
#             splashScreen()
#         elif backList[-1] == "004":
#             registerAdmin()
#         elif backList[-1] == "005":
#             adminPage1()
#         elif backList[-1] == "006":
#             adminPage2()
#         elif backList[-1] == "007":
#             addEmployeePage()
#         elif backList[-1] == "008":
#             addEmployeeNextPage()
#         elif backList[-1] == "009":
#             signingPage()
#     except IndexError:
#         print("Empty List")
#         firstPage()


# firstPage()
#backBtn.config(command=switch)
firstPage()

v.app.mainloop()
