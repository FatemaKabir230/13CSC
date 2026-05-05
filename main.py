import tkinter
from tkinter import*
root = Tk()
root.geometry("700x400")
root.resizable(False,False)


root = tkinter.Tk
frame = tkinter.Frame(root)
frame.pack()

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your username")

def username_data():
    username = username_entry.get()
    print(username, "Let's start calculating your rank score, click the button to begin")

username_info_frame = tkinter.LabelFrame(frame, text="Enter your username")
username_info_frame.grid(row=1, column=2, padx=5, pady=5)

username_entry =  tkinter.Entry(frame, text="Username:")
username_entry.grid(row=1, column=2, padx=5, pady=5)


def myClick():
    myLabel = Label(root, text="Enter your username here:")
    MyLabel = "Username:" + e.get()
    myLabel.pack()

myLabel = Label(root, text="welcome to the rank score calculator", command=myClick)
myLabel.pack()

myButton = Button(root, text="click to start calculating")
myButton.pack()


root.mainloop()