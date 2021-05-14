# 100 days with Python 
# Quiz Game
# DAY 17  
# OOP first steps

from hangman_arch import question_data

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:

    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.q_list)

    def next_question(self):
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True or False?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"It was a right answer!")
        else:
            print(f"It was an incorrect answer!")
        print(f"Your score is {self.q_number}/{self.score}")


question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("It is the end of the quiz.")
print(f"Your score is : {quiz.score} for {quiz.q_number} answers")