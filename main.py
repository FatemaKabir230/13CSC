from tkinter import*
root = Tk()
root.geometry("600x400")


#Create home screen
class Intro:
    def __init__(self, parent):
     background_color= "black"
     self.intro_frame = Frame(parent, bg=background_color)
     self.intro_grid = ("nsew")

     self.top_label = Label(self.intro_frame, text="hi")



class Calculation:
    def __init__(self, parent):
     background_color= "white"
     self.calculation_frame = Frame(parent, bg=background_color)
     self.calculation_grid = ("nsew")



class Final:
    def __init__(self, parent):
     background_color= "white"
     self.final_frame = Frame(parent, bg=background_color)
     self.final_grid = ("nsew")






#Launches the home screen
if __name__ == "__main__":
    root.title("Rank Score Calculator")
    program_instance = Intro(root)
    root.mainloop()