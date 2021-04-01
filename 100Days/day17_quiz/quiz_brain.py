class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def questions_remain(self):
        """adding a 'return' effectively makes the below condition a Boolean (as opposed to writing a whole T/F loop)"""
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"Well done on completing the quiz,\nYour final score is {self.score}/{self.question_number}\n")
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        """from the above method, retrieve a question from the list 'question_bank', 
        at the list location 'question_number', & assign it to 'current_question'."""
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.question_text} (T/F?) ").title()
        self.check_answer(answer, current_question.answer_text)
        

    def check_answer(self, answer, correct_answer):
        if correct_answer == answer:
            self.score += 1
            print("Correct")
        else:
            print("Incorrect")
        print(f"Current Score: {self.score}/{self.question_number}\n")
    
