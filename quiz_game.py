import requests
import random
import json
from typing import List, Dict


class Question:
    def __init__(self, question: str, correct_answer: str, incorrect_answers: List[str]):
        self.question = question
        self.correct_answer = correct_answer
        self.options = incorrect_answers + [correct_answer]
        random.shuffle(self.options)

    def is_correct(self, answer: str) -> bool:
        return answer.lower() == self.correct_answer.lower()

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")


class QuizGame:
    def __init__(self, num_questions: int = 10):
        self.num_questions = num_questions
        self.questions = self.fetch_questions()
        self.score = 0

    def fetch_questions(self) -> List[Question]:
        try:
            url = f"https://opentdb.com/api.php?amount={self.num_questions}&type=multiple"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            return [Question(q['question'], q['correct_answer'], q['incorrect_answers'])
                    for q in data['results']]
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            print(f"Error fetching questions from API: {e}")
            print("Using local backup questions instead.")
            return self.get_local_questions()


    def play(self):
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}:")
            question.display()
            user_answer = input("Enter your answer (1-4): ")

            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                user_answer = question.options[int(user_answer) - 1]
                if question.is_correct(user_answer):
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong. The correct answer was: {question.correct_answer}")
            else:
                print("Invalid input. Skipping this question.")

            print(f"Current score: {self.score}/{i}")

        print(f"\nQuiz complete! Your final score is: {self.score}/{self.num_questions}")


def get_num_questions() -> int:
    while True:
        try:
            num_questions = int(input("How many questions would you like? (1-10): "))
            if 1 <= num_questions <= 10:
                return num_questions
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")


# Main game loop
if __name__ == "__main__":
    print("Welcome to the Robust Multiple Choice Quiz Game!")
    print("Answer each question by entering the number of your choice (1-4).")
    print("Let's begin!\n")

    num_questions = get_num_questions()

    while True:
        game = QuizGame(num_questions)
        game.play()

        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")
