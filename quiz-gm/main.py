from question_model import Question
from data import question_data, question_data1
from quiz_brain import QuizBrain

question_bank = list()

for i in range(len(question_data1)):
    question = Question(question_data1[i]["question"], question_data1[i]["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
