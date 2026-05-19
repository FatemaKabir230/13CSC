import tkinter
from tkinter import*
from types import new_class
from PIL import ImageTk, Image

root = Tk()
root.geometry("800x500")
root.resizable(True,True)
root.title("Rank Score Calculator Intro")

frame = Frame(root, bg="#FFE27A")
frame.place(relwidth=1, relheight=1)

box=Frame(root, bg="#CEECF6")
box.place(relx=0.5, rely= 0.5, relwidth=0.9, relheight=0.8, anchor="center")

myLabel = Label(frame, text="Rank Score Calculator", bg="#FFE27A")
myLabel.place(relx=0.5, rely=0.05)

myLabel = Label(box, text="Enter your username:", bg="#CEECF6")
myLabel.place(relx=0.3, rely=0.5, )

username_entry =  tkinter.Entry(box)
username_entry.place(relx=0.5, rely=0.5)


def submit_username():
    username = username_entry.get()

    root.Tk=new_class()
    frame = Frame(new_class)
    frame.place(relwidth=1, relheight=1)

    box = Frame(new_class)
    box.place(relx=0.55, rely=0.53, relwidth=0.8, relheight=0.6)

    subjects = ["Accounting","Adult Education","Agricultural and Horticultural Science","Agribusiness","Art History","Biology","Business and Management","Business Studies","Chemistry","Chinese (Mandarin)",
    "Classical Studies","Cook Islands Māori","Core Skills","Dance","Design and Visual Communication","Digital Technologies","Drama","Driver Licence (Class 1)",
    "Early Childhood Education","Earth and Space Science","Economics","Education for Sustainability","English","English for Academic Purposes","English Language",
    "Field Māori","French","Gagana Sāmoa","Gagana Tokelau","Geography","German","Hangarau","Hauora","Health","History","Home Economics","Japanese","Korean",
    "Latin","Lea Faka-Tonga","Legal Studies","Literacy - Reading","Literacy - Writing","Mathematics and Statistics","Media Studies","Music","New Zealand Sign Language",
    "Ngā Mahi a te Rēhia","Numeracy","Pacific Studies","Pāngarau","Physical Education","Physics","Psychology","Pūtaiao","Religious Studies","Samoan","Science",
    "Social Studies","Sociology","Spanish","Supported Learning","Te Ao Haka","Technology","Te Reo Māori","Te Reo Māori Kūki ‘Āirani","Te Reo Matatini","Te Reo Pāngarau",
    "Te Reo Rangatira","Tikanga ā-Iwi","Toi Ataata","Toi Puoro","Vagahau Niue","Visual Arts"]

    selected_option = StringVar()
    selected_option.set("Select a subject")

    dropdown1 = OptionMenu(frame, selected_option, *subjects)
    dropdown1.place(relx=0.06, rely=0.2, anchor="center")


submit_button=Button(root, text="Submit/Start", command=submit_username)
submit_button.place(relx=0.5, rely=0.8)




root.mainloop()