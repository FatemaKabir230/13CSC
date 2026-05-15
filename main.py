import tkinter
from tkinter import*
from types import new_class

root = Tk()
root.geometry("700x400")
root.resizable(False,False)

#Creating new window after submit button is clicked
def new_window():
    new_root = Toplevel()
    old_root.destroy()
old_root = Tk()

frame = Frame(root)
frame.grid()

subjects={}

myLabel = tkinter.LabelFrame(frame, text="Rank Score Calculator")
myLabel.grid(row=0, column=5, padx=5, pady=10)

info_button = tkinter.LabelFrame(frame, text="Click here for program information")
info_button.grid(row=5, column=0)

username_entry =  tkinter.Entry(frame, text="Username:")
username_entry.grid(row=1, column=1, padx=5, pady=2)

#separate entry username
#username_entry =  tkinter.Entry(e.get())
#username_entry.grid(row=1, column=2, padx=5, pady=5)



def username_data():
    username = username_entry.get()
    print(username, "Let's start calculating your rank score, click the button to begin")

done_button=Button(root, text="Click to register username", command=username_data())
done_button.grid(row=1, column=3)

submit_button=Button(root, text="Submit/Start", command=new_window())
submit_button.grid(row=5, column=1)




root.mainloop()