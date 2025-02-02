class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def retriever(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number} {item.text}. (True/False)?: ")
        self.check_answer(user_answer, item.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
            print(f"Your score is: {self.score}/{self.question_number}.")
        else:
            print("That's worng.")
        print(f"The correct answer is: {correct_answer}")
