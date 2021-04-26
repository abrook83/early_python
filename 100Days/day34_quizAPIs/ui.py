from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="question text", fill="black", font=("arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)
        
        true_image = PhotoImage(file="100Days\day34_quizAPIs\images/true.png")
        self.true_button = Button(image=true_image, width=100, height=97, command=self.select_true, highlightthickness=0)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        false_image = PhotoImage(file="100Days\day34_quizAPIs\images/false.png")
        self.false_button = Button(image=false_image, width=100, height=97, command=self.select_false, highlightthickness=0)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)        

        self.score_text = Label(text=f"Score:", fg="white", bg=THEME_COLOR, font=("arial", 12, "normal"))
        self.score_text.grid(column=1, row=0, padx=20, pady=20)

        self.get_next_question()     

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    
    def select_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def select_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
        
