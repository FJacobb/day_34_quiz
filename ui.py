
from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, QuizBrain: QuizBrain):
        self.window = Tk()
        self.quiz = QuizBrain
        self.bg = PhotoImage(file="images/backgroundldpi.png")
        self.card = PhotoImage(file="images/wordldpi.png")
        self.right = PhotoImage(file="images/rightldpi.png")
        self.rightoff = PhotoImage(file="images/rightoffldpi.png")
        self.wrong = PhotoImage(file="images/wrongldpi.png")
        self.wrongoff = PhotoImage(file="images/wrongoffldpi.png")
        self.right_answer = PhotoImage(file="images/right_answerldpi.png")
        self.wrong_answer = PhotoImage(file="images/wrong_answerldpi.png")
        self.window.geometry("448x336")
        self.window.title("Quizzila")
        self.canvar = Canvas(width=450, height=338)
        self.canvar.place(x=-2,y=-2)
        self.canvar.create_image(225, 174, image=self.bg)
        self.card_place= self.canvar.create_image(225, 174, image=self.card)
        self.score = self.canvar.create_text(380, 26, text=f"Score:{self.quiz.score}",font=("Space Quest", 18), fill="white")
        self.button_right = Button(image=self.right, border=0,bg="#24126a", command=self.right_butten_return)
        self.button_right.place(x=70, y=285)
        self.button_right.bind("<Enter>", self.right_hover_off)
        self.button_right.bind("<Leave>", self.right_hover_on)
        self.question = self.canvar.create_text(225, 174, text="", width=320, font=("Space Quest", 18), fill="white")
        self.button_wrong = Button(image=self.wrong, border=0, bg="#24126a", command=self.wrong_butten_return)
        self.button_wrong.place(x=320, y=285)
        self.button_wrong.bind("<Enter>", self.wrong_hover_off)
        self.button_wrong.bind("<Leave>", self.wrong_hover_on)
        self.receive_question(self.quiz.next_question())
        self.window.mainloop()

    def right_hover_off(self, e):
        self.button_right["image"] = self.rightoff
    def right_hover_on(self,e):
        self.button_right["image"] = self.right

    def wrong_hover_off(self, e):
        self.button_wrong["image"] = self.wrongoff

    def wrong_hover_on(self, e):
        self.button_wrong["image"] = self.wrong
    def receive_question(self, question):
        self.canvar.itemconfig(self.card_place, image=self.card)
        self.canvar.itemconfig(self.question, text=question)
    def right_butten_return(self):
        self.answer = self.quiz.check_answer("True")
        self.color()

    def wrong_butten_return(self):
        self.answer= self.quiz.check_answer("False")
        self.color()
    def color(self):
        if self.answer:
            self.canvar.itemconfig(self.card_place, image=self.right_answer)

        else:
            self.canvar.itemconfig(self.card_place, image=self.wrong_answer)
        self.canvar.after(1000,self.call_back)
    def call_back(self):
        if self.quiz.still_has_questions():
            self.canvar.itemconfig(self.score,text=f"Score:{self.quiz.score}")
            self.receive_question(self.quiz.next_question())
        else:
            self.receive_question("you have reached the end of the quiz")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")