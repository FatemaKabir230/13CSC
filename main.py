import tkinter
from ctypes.wintypes import LANGID
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

#Image1
image = Image.open("stretch 1.png")
image = image.resize((300, 300))
img = ImageTk.PhotoImage(image)
label = Label(box, image=img, bg="#CEECF6")
label.place(relx=0.2, rely=0.8, anchor="center")

#Image2
image = Image.open("worker 1.png")
image = image.resize((260, 260))
img1 = ImageTk.PhotoImage(image)
label = Label(box, image=img1, bg="#CEECF6")
label.place(relx=0.8, rely=0.8, anchor="center")


def submit_username():
    #username = username_entry.get()
    #frame.place_forget()
    #root.place_forget()

    new_class = Toplevel()
    new_class.title("Entry of Subjects/Credits")
    new_class.configure(bg="#CEECF6")
    new_class.resizable(True,True)


    frame = Frame(new_class, bg="#CEECF6")
    frame.place(relwidth=1, relheight=1)

    box = Frame(new_class, bg="#EEEEEE")
    box.place(relx=0.53, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")

    subjects = ["Accounting","Adult Education","Agricultural and Horticultural Science","Agribusiness","Art History","Biology","Business and Management","Business Studies","Chemistry","Chinese (Mandarin)",
    "Classical Studies","Cook Islands Māori","Core Skills","Dance","Design and Visual Communication","Digital Technologies","Drama","Driver Licence (Class 1)",
    "Early Childhood Education","Earth and Space Science","Economics","Education for Sustainability","English","English for Academic Purposes","English Language",
    "Field Māori","French","Gagana Sāmoa","Gagana Tokelau","Geography","German","Hangarau","Hauora","Health","History","Home Economics","Japanese","Korean",
    "Latin","Lea Faka-Tonga","Legal Studies","Literacy - Reading","Literacy - Writing","Mathematics and Statistics","Media Studies","Music","New Zealand Sign Language",
    "Ngā Mahi a te Rēhia","Numeracy","Pacific Studies","Pāngarau","Physical Education","Physics","Psychology","Pūtaiao","Religious Studies","Samoan","Science",
    "Social Studies","Sociology","Spanish","Supported Learning","Te Ao Haka","Technology","Te Reo Māori","Te Reo Māori Kūki ‘Āirani","Te Reo Matatini","Te Reo Pāngarau",
    "Te Reo Rangatira","Tikanga ā-Iwi","Toi Ataata","Toi Puoro","Vagahau Niue","Visual Arts"]


    n_ach = Label(new_class, text="Not Achieved:", bg="#CEECF6")
    n_ach.place(relx=0.2, rely=0.03, anchor="center")
    ach = Label(new_class, text="Achieved:", bg="#CEECF6")
    ach.place(relx=0.4, rely=0.03, anchor="center")
    mer = Label(new_class, text="Merit:", bg="#CEECF6")
    mer.place(relx=0.6, rely=0.03, anchor="center" )
    ex = Label(new_class, text="Excellence:", bg="#CEECF6")
    ex.place(relx=0.8, rely=0.03, anchor="center" )


    #Drowdown boxes
    selected_option = StringVar()
    selected_option.set("Select a subject")

    dropdown1 = OptionMenu(new_class, selected_option, *subjects)
    dropdown1.place(relx=0.04, rely=0.2, anchor="center")

    dropdown2 = OptionMenu(new_class, selected_option, *subjects)
    dropdown2.place(relx=0.04, rely=0.35, anchor="center")

    dropdown3 = OptionMenu(new_class, selected_option, *subjects)
    dropdown3.place(relx=0.04, rely=0.5, anchor="center")

    dropdown4 = OptionMenu(new_class, selected_option, *subjects)
    dropdown4.place(relx=0.04, rely=0.65, anchor="center")

    dropdown5 = OptionMenu(new_class, selected_option, *subjects)
    dropdown5.place(relx=0.04, rely=0.8, anchor="center")

    s1e = tkinter.Entry(new_class, width=20)
    s1e.place(relx=0.2, rely=0.2, anchor="center")
    s1e = tkinter.Entry(new_class)
    s1e.place(relx=0.2, rely=0.35, anchor="center")
    s1e = tkinter.Entry(new_class)
    s1e.place(relx=0.2, rely=0.5, anchor="center")
    s1e = tkinter.Entry(new_class)
    s1e.place(relx=0.2, rely=0.65, anchor="center")
    s1e = tkinter.Entry(new_class)
    s1e.place(relx=0.2, rely=0.8, anchor="center")

    s2e = tkinter.Entry(new_class)
    s2e.place(relx=0.4, rely=0.2, anchor="center")
    s2e = tkinter.Entry(new_class)
    s2e.place(relx=0.4, rely=0.35, anchor="center")
    s2e = tkinter.Entry(new_class)
    s2e.place(relx=0.4, rely=0.5, anchor="center")
    s2e = tkinter.Entry(new_class)
    s2e.place(relx=0.4, rely=0.65, anchor="center")
    s2e = tkinter.Entry(new_class)
    s2e.place(relx=0.4, rely=0.8, anchor="center")

    s3e = tkinter.Entry(new_class)
    s3e.place(relx=0.6, rely=0.2, anchor="center")
    s3e = tkinter.Entry(new_class)
    s3e.place(relx=0.6, rely=0.35, anchor="center")
    s3e = tkinter.Entry(new_class)
    s3e.place(relx=0.6, rely=0.5, anchor="center")
    s3e = tkinter.Entry(new_class)
    s3e.place(relx=0.6, rely=0.65, anchor="center")
    s3e = tkinter.Entry(new_class)
    s3e.place(relx=0.6, rely=0.8, anchor="center")

    s4e = tkinter.Entry(new_class)
    s4e.place(relx=0.8, rely=0.2, anchor="center")
    s4e = tkinter.Entry(new_class)
    s4e.place(relx=0.8, rely=0.35, anchor="center")
    s4e = tkinter.Entry(new_class)
    s4e.place(relx=0.8, rely=0.5, anchor="center")
    s4e = tkinter.Entry(new_class)
    s4e.place(relx=0.8, rely=0.65, anchor="center")
    s4e = tkinter.Entry(new_class, )
    s4e.place(relx=0.8, rely=0.8, anchor="center")

    def final_window():
        results_window = Toplevel()
        results_window.title("Entry of Subjects/Credits")
        results_window.configure(bg="#CEECF6")
        results_window.resizable(True, True)

        frame = Frame(results_window, bg="#CEECF6")
        frame.place(relwidth=1, relheight=1)

        box = Frame(results_window, bg="white")
        box.place(relx=0.53, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")


    results_button = Button(frame, text="Done", command=final_window)
    results_button.place(relx=0.5, rely=0.8)

submit_button=Button(root, text="Submit/Start", command=submit_username)
submit_button.place(relx=0.5, rely=0.8)






root.mainloop()