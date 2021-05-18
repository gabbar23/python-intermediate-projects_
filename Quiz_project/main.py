from data import question_data
from question_model import Question
from quiz_brain import QuizBank
question_bank=[]
for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question=Question(q_text=question_text,a_text=question_answer)
    question_bank.append(new_question)


quiz=QuizBank(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your score is {quiz.score}")