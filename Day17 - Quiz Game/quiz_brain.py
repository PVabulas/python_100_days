from time import sleep


def print_zzz(*args):
    print(*args)
    sleep(0.5)


class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {question.text}. (True/False)?:")
        self.check_answer(response, question.answer)

    def check_answer(self, response, answer):
        if response.lower() == answer.lower():
            print_zzz("That is correct!")
            self.score += 1
        else:
            print_zzz(f"Incorrect, the right answer is {answer}")
        print_zzz(f"Your score is {self.score}/{self.question_number}")
        print("\n")
