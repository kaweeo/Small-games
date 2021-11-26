import question_model
import data
import quiz_brain

question_bank = []
for dic in data.question_data:
    q = dic["question"]
    a = dic["correct_answer"]
    qa = question_model.Question(q, a)
    question_bank.append(qa)
print(question_bank)
quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.retriever()

print("You have completed the quiz!!!")
print(f"Your final score was {quiz.score}/{len(question_bank)}")