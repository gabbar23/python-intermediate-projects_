
class QuizBank:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score=0

    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        answer=input(f"Q{self.question_number} {current_question.text} True/False ")
        self.check_answer(answer,current_question.answer)


    def check_answer(self,answer,current_answer):
        if answer.lower()==current_answer.lower():
            self.score+=1
            print("You got it right!")
        else:
            print("That was a Wrong answer!")





