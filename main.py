import tkinter
from ctypes.wintypes import LANGID
from tkinter import*
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
myLabel.place(relx=0.45, rely=0.05)

myLabel = Label(box, text="Enter your username:", bg="#CEECF6")
myLabel.place(relx=0.3, rely=0.3, )

username_entry =  tkinter.Entry(box)
username_entry.place(relx=0.5, rely=0.3)

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

    box = Frame(new_class, bg="white")
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

    subject1 = StringVar()
    subject1.set("Select a subject")

    subject2 = StringVar()
    subject2.set("Select a subject")

    subject3 = StringVar()
    subject3.set("Select a subject")

    subject4 = StringVar()
    subject4.set("Select a subject")

    subject5 = StringVar()
    subject5.set("Select a subject")

    dropdown1 = OptionMenu(new_class, subject1, selected_option, *subjects)
    dropdown1.place(relx=0.04, rely=0.2, anchor="center")

    dropdown2 = OptionMenu(new_class, subject2, selected_option, *subjects)
    dropdown2.place(relx=0.04, rely=0.35, anchor="center")

    dropdown3 = OptionMenu(new_class, subject3, selected_option, *subjects)
    dropdown3.place(relx=0.04, rely=0.5, anchor="center")

    dropdown4 = OptionMenu(new_class, subject4, selected_option, *subjects)
    dropdown4.place(relx=0.04, rely=0.65, anchor="center")

    dropdown5 = OptionMenu(new_class, subject5, selected_option, *subjects)
    dropdown5.place(relx=0.04, rely=0.8, anchor="center")


    #Subject and credit entry widgets
    s1na = tkinter.Entry(new_class, width=20)
    s1na.place(relx=0.2, rely=0.2, anchor="center")
    s2na = tkinter.Entry(new_class)
    s2na.place(relx=0.2, rely=0.35, anchor="center")
    s3na = tkinter.Entry(new_class)
    s3na.place(relx=0.2, rely=0.5, anchor="center")
    s4na = tkinter.Entry(new_class)
    s4na.place(relx=0.2, rely=0.65, anchor="center")
    s5na = tkinter.Entry(new_class)
    s5na.place(relx=0.2, rely=0.8, anchor="center")

    s1a = tkinter.Entry(new_class)
    s1a.place(relx=0.4, rely=0.2, anchor="center")
    s2a = tkinter.Entry(new_class)
    s2a.place(relx=0.4, rely=0.35, anchor="center")
    s3a = tkinter.Entry(new_class)
    s3a.place(relx=0.4, rely=0.5, anchor="center")
    s4a = tkinter.Entry(new_class)
    s4a.place(relx=0.4, rely=0.65, anchor="center")
    s5a = tkinter.Entry(new_class)
    s5a.place(relx=0.4, rely=0.8, anchor="center")

    s1m = tkinter.Entry(new_class)
    s1m.place(relx=0.6, rely=0.2, anchor="center")
    s2m = tkinter.Entry(new_class)
    s2m.place(relx=0.6, rely=0.35, anchor="center")
    s3m = tkinter.Entry(new_class)
    s3m.place(relx=0.6, rely=0.5, anchor="center")
    s4m = tkinter.Entry(new_class)
    s4m.place(relx=0.6, rely=0.65, anchor="center")
    s5m = tkinter.Entry(new_class)
    s5m.place(relx=0.6, rely=0.8, anchor="center")

    s1e = tkinter.Entry(new_class)
    s1e.place(relx=0.8, rely=0.2, anchor="center")
    s2e = tkinter.Entry(new_class)
    s2e.place(relx=0.8, rely=0.35, anchor="center")
    s3e = tkinter.Entry(new_class)
    s3e.place(relx=0.8, rely=0.5, anchor="center")
    s4e = tkinter.Entry(new_class)
    s4e.place(relx=0.8, rely=0.65, anchor="center")
    s5e = tkinter.Entry(new_class, )
    s5e.place(relx=0.8, rely=0.8, anchor="center")

    # Group all entries for calculation prioritization


    total_na = sum(int(e.get() or 0) for e in [s1na, s2na, s3na, s4na, s5na])
    total_a = sum(int(e.get() or 0) for e in [s1a, s2a, s3a, s4a, s5a])
    total_m = sum(int(e.get() or 0) for e in [s1m, s2m, s3m, s4m, s5m])
    total_e = sum(int(e.get() or 0) for e in [s1m, s2m, s3m, s4m, s5m])

    max_credits_left = 80

    e_taken = min(total_e, max_credits_left)
    max_credits_left -= e_taken

    m_taken = min(total_e, max_credits_left)
    max_credits_left -= m_taken

    a_taken = min(total_e, max_credits_left)
    max_credits_left -= a_taken

    na_taken = min(total_e, max_credits_left)
    max_credits_left -= na_taken

    rank_score = (
        e_taken * 4 +
        m_taken * 3 +
        a_taken * 2 +
        na_taken * 1
    )



    # Launches results screen
    def final_window():
        results_window = Toplevel()
        results_window.title("Rank Score Results and Desired Degree")
        results_window.configure(bg="#CEECF6")
        results_window.resizable(True, True)
        results_window.geometry("700x400    ")

        frame = Frame(results_window, bg="#CEECF6")
        frame.place(relwidth=1, relheight=1)

        box = Frame(results_window, bg="white")
        box.place(relx=0.53, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")


        total_rank_score = Label(results_window, text=rank_score, bg="#CEECF6")
        total_rank_score.place(relx=0.5, rely=0.1, anchor="center")

        # Breakdown of total credits of each grade
        not_achieved_credits = Label(results_window, text="NOT ACHIEVED:", bg="#CEECF6")
        not_achieved_credits.place(relx=0.15, rely=0.1, anchor="center")
        achieved_credits = Label(results_window, text="ACHIEVED:", bg="#CEECF6")
        achieved_credits.place(relx=0.35, rely=0.1, anchor="center")
        merit_credits = Label(results_window, text="MERIT:", bg="#CEECF6")
        merit_credits.place(relx=0.55, rely=0.1, anchor="center")
        excellence_credits = Label(results_window, text="EXCELLENCE:", bg="#CEECF6")
        excellence_credits.place(relx=0.75, rely=0.1, anchor="center")

        #Displays rank score to user + uses their entered username from home page
        username = username_entry.get()
        user_rank_score_label = Label(results_window, text=username + "your rank score is:", bg="#CEECF6")
        user_rank_score_label.place(relx=0.15, rely=0.3, anchor="center")
        #Display total rank score value (whole value)
        user_rank_score = Label(results_window, text="#:", bg="#CEECF6")
        user_rank_score.place(relx=0.15, rely=0.3, anchor="center")

        # Label to say whether they got their chosen rank score or not
        comparision_label = Label(results_window, text="Your rank score is X lower/higher than chosen rank score", bg="#CEECF6")
        comparision_label.place(relx=0.5, rely=0.5, anchor="center", )

        #Code to meet desired rank score




        #Dictionary of UOA undergrad degrees with assigned value as needed rank score
        #pay attention to changed degree rank scores (biomed and health sci) + new degrees like science field - cells etc
        UOA_undergrad_degrees= { "Bachelor of Commerce (BCom)": 200, "Bachelor of Property (BProp)": 165, "Bachelor of Early Childhood Studies (BECSt)": 150,
        "Bachelor of Education (Tchg)": 150, "Bachelor of Education (TESOL)": 150, "Bachelor of Architectural Studies (BAS)": 230,
        "Bachelor of Design (BDes)": 180, "Bachelor of Engineering (Honours) (BE(Hons))": 250, "Bachelor of Urban Planning(Honours) (BUrbPlan(Hons))": 180,
        "Bachelor of Health Sciences(BHSc)": 250, "Bachelor of Nursing (BNurs)": 230, "Bachelor of Sport Health and Physical Education (BSportHPE)": 150,
        "Bachelor of Arts (BA)": 150, "Bachelor of Communication (BC)": 165, "Bachelor of Global Studies (BGlobalSt)": 180, "Bachelor of Global Studies (BGlobalSt)": 180,
        "Bachelor of Dance Studies (BDanceSt)": 150, "Bachelor of Music (BMus)": 150, "Bachelor of Music (BMus)": 150, "Bachelor of Science (BSc)": 200,
        "Bachelor of Health Sciences (BHSc)": 200}


#degrees which require to finish bachelor of science first year then - Bachelor of Medical Imaging (Honours) (BMedImag(Hons)),
#Bachelor of Medicine and Bachelor of Surgery (MBChB), optometry, and
        #Drop down menu for choosing UOA degree
        degree_selected_option = StringVar()
        degree_selected_option.set("Select your desired degree of admission, note that some degrees may be omitted due to having to qualify/finishing for a  BSc first")
        degree_1_dropdown = OptionMenu(results_window, degree_selected_option, *UOA_undergrad_degrees)
        degree_1_dropdown.place(relx=0.04, rely=0.2, anchor="center")



    # Entry page done button which when clicked launches results window, and destroys entry page
    results_button = Button(new_class, text="Done", command=lambda: [final_window(), new_class.destroy()])
    results_button.place(relx=0.5, rely=0.8)

#Home page submit button which when clicked launches entry page and destroys home page
submit_button=Button(box, text="Submit/Start", command=lambda: [submit_username(), root.withdraw()])
submit_button.place(relx=0.5, rely=0.8)






root.mainloop()