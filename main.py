from tkinter import*
root = Tk()
root.geometry("700x400")
root.resizable(False,False)

e = Entry(root, width=50)
e.pack()

def myClick():
    username = "Enter your username" + e.get()
    myLabel = Label(root, text="asd" )
    myLabel.pack()

myLabel = Label(root, text="welcome to the rank score calculator",)
myLabel.pack()

myButton = Button(root, text="click to start calculating")
myButton.pack()

#2w32
root.mainloop()