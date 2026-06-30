import tkinter
from ctypes.wintypes import LANGID
from tkinter import*
from PIL import ImageTk, Image
from tkextrafont import Font

root = Tk()
root.geometry("1200x700")
root.resizable(True,True)
root.title("Rank Score Calculator Intro")

frame = Frame(root, bg="#FFE27A")
frame.place(relwidth=1, relheight=1)

box=Frame(root, bg="#CEECF6")
box.place(relx=0.5, rely= 0.5, relwidth=0.9, relheight=0.8, anchor="center")

font = ("Nanum-Pen", 20)

myLabel = Label(frame, text="What's Your Rank?", font="Tahoma", bg="#FFE27A")
myLabel.place(relx=0.45, rely=0.05)

myLabel = Label(box, text="Name:",font="Tahoma",  bg="#CEECF6")
myLabel.place(relx=0.35, rely=0.3, )

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

    new_class = Toplevel()
    new_class.title("Entry of Subjects/Credits")
    new_class.configure(bg="#CEECF6")
    new_class.resizable(True,True)
    new_class.geometry("1200x700")


    frame = Frame(new_class, bg="#CEECF6")
    frame.place(relwidth=1, relheight=1)

    box = Frame(new_class, bg="white")
    box.place(relx=0.55, rely=0.5, relwidth=0.8, relheight=0.8, anchor="center")

    subjects = ["Accounting","Adult Education","Agricultural and Horticultural Science","Agribusiness","Art History","Biology","Business and Management","Business Studies","Chemistry","Chinese (Mandarin)",
    "Classical Studies","Cook Islands Māori","Core Skills","Dance","Design and Visual Communication","Digital Technologies","Drama","Driver Licence (Class 1)",
    "Early Childhood Education","Earth and Space Science","Economics","Education for Sustainability","English","English for Academic Purposes","English Language",
    "Field Māori","French","Gagana Sāmoa","Gagana Tokelau","Geography","German","Hangarau","Hauora","Health","History","Home Economics","Japanese","Korean",
    "Latin","Lea Faka-Tonga","Legal Studies","Literacy - Reading","Literacy - Writing","Mathematics and Statistics","Media Studies","Music","New Zealand Sign Language",
    "Ngā Mahi a te Rēhia","Numeracy","Pacific Studies","Pāngarau","Physical Education","Physics","Psychology","Pūtaiao","Religious Studies","Samoan","Science",
    "Social Studies","Sociology","Spanish","Supported Learning","Te Ao Haka","Technology","Te Reo Māori","Te Reo Māori Kūki ‘Āirani","Te Reo Matatini","Te Reo Pāngarau",
    "Te Reo Rangatira","Tikanga ā-Iwi","Toi Ataata","Toi Puoro","Vagahau Niue","Visual Arts"]


    n_ach = Label(new_class, text="Not Achieved:", font="Tahoma", bg="#CEECF6")
    n_ach.place(relx=0.2, rely=0.03, anchor="center")
    ach = Label(new_class, text="Achieved:", font="Tahoma", bg="#CEECF6")
    ach.place(relx=0.4, rely=0.03, anchor="center")
    mer = Label(new_class, text="Merit:", font="Tahoma", bg="#CEECF6")
    mer.place(relx=0.6, rely=0.03, anchor="center" )
    ex = Label(new_class, text="Excellence:", font="Tahoma", bg="#CEECF6")
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
    dropdown1.place(relx=0.07, rely=0.2, anchor="center")

    dropdown2 = OptionMenu(new_class, subject2, selected_option, *subjects)
    dropdown2.place(relx=0.07, rely=0.35, anchor="center")

    dropdown3 = OptionMenu(new_class, subject3, selected_option, *subjects)
    dropdown3.place(relx=0.07, rely=0.5, anchor="center")

    dropdown4 = OptionMenu(new_class, subject4, selected_option, *subjects)
    dropdown4.place(relx=0.07, rely=0.65, anchor="center")

    dropdown5 = OptionMenu(new_class, subject5, selected_option, *subjects)
    dropdown5.place(relx=0.07, rely=0.8, anchor="center")


    #Subject and credit entry widgets
    s1na = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s1na.place(relx=0.2, rely=0.2, anchor="center")
    s2na = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s2na.place(relx=0.2, rely=0.35, anchor="center")
    s3na = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s3na.place(relx=0.2, rely=0.5, anchor="center")
    s4na = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s4na.place(relx=0.2, rely=0.65, anchor="center")
    s5na = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s5na.place(relx=0.2, rely=0.8, anchor="center")

    s1a = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s1a.place(relx=0.4, rely=0.2, anchor="center")
    s2a = tkinter.Entry(new_class, width=10,highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s2a.place(relx=0.4, rely=0.35, anchor="center")
    s3a = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s3a.place(relx=0.4, rely=0.5, anchor="center")
    s4a = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s4a.place(relx=0.4, rely=0.65, anchor="center")
    s5a = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s5a.place(relx=0.4, rely=0.8, anchor="center")

    s1m = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s1m.place(relx=0.6, rely=0.2, anchor="center")
    s2m = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s2m.place(relx=0.6, rely=0.35, anchor="center")
    s3m = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s3m.place(relx=0.6, rely=0.5, anchor="center")
    s4m = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s4m.place(relx=0.6, rely=0.65, anchor="center")
    s5m = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s5m.place(relx=0.6, rely=0.8, anchor="center")

    s1e = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s1e.place(relx=0.8, rely=0.2, anchor="center")
    s2e = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s2e.place(relx=0.8, rely=0.35, anchor="center")
    s3e = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s3e.place(relx=0.8, rely=0.5, anchor="center")
    s4e = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s4e.place(relx=0.8, rely=0.65, anchor="center")
    s5e = tkinter.Entry(new_class, width=10, highlightbackground="#CEECF6", highlightthickness=2, highlightcolor="#FFE27A")
    s5e.place(relx=0.8, rely=0.8, anchor="center")

    #Group all user entries for validation
    all_entries = [s1na, s1a, s1m, s1e,
                   s2na, s2a, s2m, s2e,
                   s3na, s3a, s3m, s3e,
                   s4na, s4a, s4m, s4e,
                   s5na, s5a, s5m, s5e]

    #Config label which will return error message if user validation fails
    done_instruction_label = Label(new_class, text="", bg="#CEECF6", font="Tahoma")
    done_instruction_label.place(relx=0.5, rely=0.93, anchor="center")

    #Function for validation
    def test_int():
        try:
            for entry in all_entries:
                int(entry.get() or 0)


        except ValueError:
            done_instruction_label.config(text="Please enter numbers only", font="Tahoma")


    # Launches results screen
    def final_window():
        results_window = Toplevel()
        results_window.title("Rank Score Results and Desired Degree")
        results_window.configure(bg="#CEECF6")
        results_window.resizable(True, True)
        results_window.geometry("1200x700")


        frame = Frame(results_window, bg="#FFE27A")
        frame.place(relwidth=1, relheight=1)

        box = Frame(results_window, bg="#CEECF6")
        box.place(relx=0.53, rely=0.5, relwidth=0.9, relheight=0.8, anchor="center")

        # Group all entries for calculation prioritization
        total_na = sum(int(e.get() or 0) for e in [s1na, s2na, s3na, s4na, s5na])
        total_a = sum(int(e.get() or 0) for e in [s1a, s2a, s3a, s4a, s5a])
        total_m = sum(int(e.get() or 0) for e in [s1m, s2m, s3m, s4m, s5m])
        total_e = sum(int(e.get() or 0) for e in [s1e, s2e, s3e, s4e, s5e])


        max_credits_left = 80

        e_taken = min(total_e, max_credits_left)
        max_credits_left -= e_taken

        m_taken = min(total_m, max_credits_left)
        max_credits_left -= m_taken

        a_taken = min(total_a, max_credits_left)
        max_credits_left -= a_taken

        na_taken = min(total_na, max_credits_left)
        max_credits_left -= na_taken

        rank_score = (
                e_taken * 4 +
                m_taken * 3 +
                a_taken * 2 +
                na_taken * 1
        )

        username = username_entry.get()

        myLabel = Label(results_window, text="What's Your Rank?", font="Tahoma", bg="#FFE27A")
        myLabel.place(relx=0.5, rely=0.05, anchor="center")

        total_cr = e_taken + m_taken + a_taken + na_taken

        total_credits = Label(results_window, text=total_cr, font="Tahoma", bg="#CEECF6")
        total_credits.place(relx=0.5, rely=0.15, anchor="center")

        # Breakdown of total credits of each grade
        not_achieved_credits = Label(results_window, text="NOT ACHIEVED:", font="Tahoma", bg="#CEECF6")
        not_achieved_credits.place(relx=0.2, rely=0.25, anchor="center")
        achieved_credits = Label(results_window, text="ACHIEVED:", font="Tahoma", bg="#CEECF6")
        achieved_credits.place(relx=0.4, rely=0.25, anchor="center")
        merit_credits = Label(results_window, text="MERIT:", font="Tahoma", bg="#CEECF6")
        merit_credits.place(relx=0.6, rely=0.25, anchor="center")
        excellence_credits = Label(results_window, text="EXCELLENCE:", font="Tahoma", bg="#CEECF6")
        excellence_credits.place(relx=0.8, rely=0.25, anchor="center")

        rank_score_label = Label(results_window, font="Tahoma", text=f"{username}, your rank score is {rank_score}", bg="#CEECF6")
        rank_score_label.place(relx=0.5, rely=0.5, anchor="center")

        not_achieved_br = Label(results_window, font="Tahoma", text=na_taken, bg="#CEECF6")
        not_achieved_br.place(relx=0.2, rely=0.35, anchor="center")
        achieved_br = Label(results_window, font="Tahoma", text=a_taken, bg="#CEECF6")
        achieved_br.place(relx=0.4, rely=0.35, anchor="center")
        merit_br = Label(results_window, font="Tahoma", text=m_taken, bg="#CEECF6")
        merit_br.place(relx=0.6, rely=0.35, anchor="center")
        excellence_br = Label(results_window, font="Tahoma", text=e_taken, bg="#CEECF6")
        excellence_br.place(relx=0.8, rely=0.35, anchor="center")





        #Dictionary of UOA undergrad degrees with assigned value as needed rank score
        #pay attention to changed degree rank scores (biomed and health sci) + new degrees like science field - cells etc
        UOA_undergrad_degrees= { "Bachelor of Commerce (BCom)": 200, "Bachelor of Property (BProp)": 165, "Bachelor of Early Childhood Studies (BECSt)": 150,
        "Bachelor of Education (Tchg)": 150, "Bachelor of Education (TESOL)": 150, "Bachelor of Architectural Studies (BAS)": 230,
        "Bachelor of Design (BDes)": 180, "Bachelor of Engineering (Honours) (BE(Hons))": 250, "Bachelor of Urban Planning(Honours) (BUrbPlan(Hons))": 180,
        "Bachelor of Health Sciences(BHSc)": 250, "Bachelor of Nursing (BNurs)": 230, "Bachelor of Sport Health and Physical Education (BSportHPE)": 150,
        "Bachelor of Arts (BA)": 150, "Bachelor of Communication (BC)": 165, "Bachelor of Global Studies (BGlobalSt)": 180, "Bachelor of Global Studies (BGlobalSt)": 180,
        "Bachelor of Dance Studies (BDanceSt)": 150, "Bachelor of Music (BMus)": 150, "Bachelor of Music (BMus)": 150, "Bachelor of Science (BSc)": 200,
        "Bachelor of Health Sciences (BHSc)": 200}

        credit_calc_option = {"Minimize Credits", "Maximize Credits"}

        credit_calc_button = StringVar()
        credit_calc_button.set("Choose calculation mode")
        credit_calc_dropdown = OptionMenu(results_window, credit_calc_button, *credit_calc_option,
                                          command=lambda: [meet_rs_1(), meet_rs_2()])
        credit_calc_dropdown.place(relx=0.9, rely=0.05, anchor="center")

        # Config labels for if rank score is met (degree 1 and 2)
        degree_meet_1 = Label(results_window, font="Tahoma", text="", bg="#CEECF6")
        degree_meet_1.place(relx=0.55, rely=0.6, anchor="center")

        degree_meet_2 = Label(results_window, font="Tahoma", text="", bg="#CEECF6")
        degree_meet_2.place(relx=0.55, rely=0.7, anchor="center")

        # Config labels for credit calculation method (degree 1 and 2)
        cr1_calc = Label(results_window, font="Tahoma", text="", bg="#CEECF6")
        cr1_calc.place(relx=0.8, rely=0.6, anchor="center")

        cr2_calc = Label(results_window, font="Tahoma", text="", bg="#CEECF6")
        cr2_calc.place(relx=0.8, rely=0.7, anchor="center")

        def meet_rs_1(selected_degree="None"):
            selected_degree = degree_selected_option.get()
            required_rank_score = UOA_undergrad_degrees[selected_degree]
            cr_left = required_rank_score - rank_score

            if cr_left <= 0:
                degree_meet_1.config(font="Tahoma", text=f"Great! You qualify for {selected_degree}")

            else:
                degree_meet_1.config(font="Tahoma", text=f"You need {cr_left} more rank score points")

                if credit_calc_button.get() == "Minimize Credits":
                    e = cr_left // 4
                    remaining = cr_left % 4
                    m = 0
                    a = 0
                    if remaining == 3:
                        m = 1
                    elif remaining == 2:
                        a = 1
                    elif remaining == 1:
                        e += 1
                    cr1_calc.config(font="Tahoma", text=f"{e}E + {m}M + {a}A")

                if credit_calc_button.get() == "Maximize Credits":
                    a = cr_left // 2
                    remaining = cr_left % 2
                    m = 0
                    if remaining == 1:
                        m = 1
                    cr1_calc.config(font="Tahoma", text=f"{a}A + {m}M")

        def meet_rs_2(selected_degree=None):
            selected_degree = degree1_selected_option.get()
            required_rank_score = UOA_undergrad_degrees[selected_degree]
            cr_left = required_rank_score - rank_score

            if cr_left <= 0:
                degree_meet_2.config(font="Tahoma", text=f"Great! You qualify for {selected_degree}")

            else:
                degree_meet_2.config(font="Tahoma", text=f"You need {cr_left} more rank score points")

                if credit_calc_button.get() == "Minimize Credits":
                    e = cr_left // 4
                    remaining = cr_left % 4
                    m = 0
                    a = 0
                    if remaining == 3:
                        m = 1
                    elif remaining == 2:
                        a = 1
                    elif remaining == 1:
                        e += 1
                    cr2_calc.config(font="Tahoma", text=f"{e}E + {m}M + {a}A")

                if credit_calc_button.get() == "Maximize Credits":
                    a = cr_left // 2
                    remaining = cr_left % 2
                    m = 0
                    if remaining == 1:
                        m = 1
                    cr2_calc.config(font="Tahoma", text=f"{a}A + {m}M")

        #Drop down menu for choosing UOA degree
        degree_selected_option = StringVar()
        degree_selected_option.set("Select your desired degree of admission")
        degree_1_dropdown = OptionMenu(results_window, degree_selected_option, *UOA_undergrad_degrees, command=meet_rs_1)
        degree_1_dropdown.place(relx=0.2, rely=0.6, anchor="center")
        degree_1_dropdown.config(font=("Tahoma", 10))

        degree1_selected_option = StringVar()
        degree1_selected_option.set("Select your desired degree of admission")
        degree_2_dropdown = OptionMenu(results_window, degree1_selected_option, *UOA_undergrad_degrees, command=meet_rs_2)
        degree_2_dropdown.place(relx=0.2, rely=0.7, anchor="center")

        # Image 3
        image = Image.open("good-job 1.png")
        image = image.resize((200, 200))
        img2 = ImageTk.PhotoImage(image)
        label = Label(results_window, image=img2, bg="#CEECF6")
        label.image = img2
        label.place(relx=0.85, rely=0.7, anchor="center")


    # Entry page done button which when clicked launches results window, and destroys entry page
    results_button = Button(new_class, font="Tahoma", text="Done", command=lambda: [test_int(), final_window(), new_class.withdraw()])
    results_button.place(relx=0.5, rely=0.95)

#Home page submit button which when clicked launches entry page and destroys home page
submit_button=Button(box, font="Tahoma", text="Submit/Start", width=20, command=lambda: [root.withdraw(), submit_username()])
submit_button.place(relx=0.45, rely=0.8)






root.mainloop()