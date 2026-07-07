class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):

        current_question = self.questions_list[self.question_number]

        user = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")

        self.question_number += 1

        self.check_answer(user,current_question.answer)


    def still_has_questions(self):

        if self.question_number < len(self.questions_list):
            return True
        else:
            return False


    def check_answer(self, user, current_question_answer):
        if user == current_question_answer.lower():
            self.score += 1
            print("Correct")

        else:
            print("Wrong")

        print(f"The correct answer was: {current_question_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

        print("\n" * 2)











