import random
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    """for each item in the 'question_data' list..."""
    question_text = question['question']
    answer_text = question['correct_answer']
    """assign both the q's and a's from each dictionary to the variables above"""
    new_question = Question(question_text, answer_text)
    """compile both into a new q/a combination"""
    question_bank.append(new_question)
    """add it to the list 'question_bank"""

quiz = QuizBrain(question_bank)
while quiz.questions_remain():
    quiz.next_question()