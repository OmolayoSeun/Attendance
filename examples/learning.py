from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learning")
root.iconbitmap('image.jpg')

num = 0


def forward():
    global myLabel
    global btBack
    global btForward
    global num
    num += 1
    myLabel.grid_forget()
    myLabel = Label(image=imageList[int(num % 4)])

    myLabel.grid(row=0, column=0, columnspan=3)
    return


def back():
    global myLabel
    global btBack
    global btForward
    global num
    num -= 1
    myLabel.grid_forget()
    myLabel = Label(image=imageList[int(num % 4)])

    myLabel.grid(row=0, column=0, columnspan=3)
    return


my_img1 = ImageTk.PhotoImage(Image.open('img/left hand.png'))
my_img2 = ImageTk.PhotoImage(Image.open('image2.png'))
my_img3 = ImageTk.PhotoImage(Image.open('image3.png'))
my_img4 = ImageTk.PhotoImage(Image.open('image4.png'))

imageList = [my_img1, my_img2, my_img3, my_img4]

myLabel = Label(image=my_img1)

btBack = Button(root, text="<<", command=back)
btExit = Button(root, text="Exit", command=root.quit)
btForward = Button(root, text=">>", command=forward)

btBack.grid(row=1, column=0)
btExit.grid(row=1, column=1)
btForward.grid(row=1, column=2)

myLabel.grid(row=0, column=0, columnspan=3)

root.mainloop()
