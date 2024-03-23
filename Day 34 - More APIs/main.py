from question_model import Question
from data import get_questions
from ui import QuizInterface

# from quiz_brain import QuizBrain
import logging
import html

logging.basicConfig(
    level=logging.CRITICAL,
    format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

question_bank = []
question_data = get_questions()
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizInterface(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
