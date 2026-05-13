import tkinter
from tkinter import*
from types import new_class

root = Tk()
root.geometry("700x400")
root.resizable(False,False)


frame = Frame(root)
frame.grid()

e = Entry(root, width=10)
e.grid()
e.insert(0, "Username")


def username_data():
    username = username_entry.get()
    print(username, "Let's start calculating your rank score, click the button to begin")

username_info_frame = tkinter.LabelFrame(frame, text="Rank Score Calculator")
username_info_frame.grid(row=0, column=5, padx=5, pady=10)

info_button = tkinter.LabelFrame(frame, text="Click here for program information")
info_button.grid(row=5, column=1)

username_entry =  tkinter.Entry(frame, text="Username:" + e.get())
username_entry.grid(row=1, column=1, padx=5, pady=2)

#separate entry username
#username_entry =  tkinter.Entry(e.get())
#username_entry.grid(row=1, column=2, padx=5, pady=5)

#Creating new window after submit is clicked
def submit_username_data():
    new_root=Toplevel()
    #old_root.destroy()


submit_button=Button(root, text="Submit/Start", command=submit_username_data())
submit_button.grid(row=5, column=1)




root.mainloop()