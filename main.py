from tkinter import*
root = Tk()
root.geometry("700x400")
root.resizable(False,False)

myLabel = Label(root, text="welcome to the rank score calculator")
myLabel.pack()

myButton = Button(root, text="click to start calculating")
myButton.pack()

#2w32
root.mainloop()