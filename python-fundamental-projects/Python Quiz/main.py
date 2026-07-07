from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
     text = question["text"]
     answer = question["answer"]
     new_questions = Question(text,answer)
     question_bank.append(new_questions)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
     quiz.next_question()



print(f"You have completed the Quiz!. Your final score is {quiz.score}/{quiz.question_number}")