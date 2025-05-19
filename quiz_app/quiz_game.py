
import requests
import random
import json
import html
from typing import List, Dict

class Question:
    def __init__(self, question: str, correct_answer: str, incorrect_answers: List[str]):
        self.question = html.unescape(question)  # Unescape HTML entities
        self.correct_answer = html.unescape(correct_answer)
        self.options = [html.unescape(ans) for ans in incorrect_answers] + [self.correct_answer]
        random.shuffle(self.options)

    def is_correct(self, answer: str) -> bool:
        return answer.lower() == self.correct_answer.lower()

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")


class QuizGame:
    def __init__(self, num_questions: int = 10, category: int = 9):
        self.num_questions = num_questions
        self.category = category
        self.questions = self.fetch_questions()
        self.score = 0

    def fetch_questions(self) -> List[Question]:
        try:
            url = f"https://opentdb.com/api.php?amount={self.num_questions}&category={self.category}&type=multiple"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data['response_code'] == 0:
                return [Question(q['question'], q['correct_answer'], q['incorrect_answers'])
                        for q in data['results']]
            else:
                print(f"API Error: {data.get('response_message', 'Unknown error')}")
                return self.get_local_questions()
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            print(f"Error fetching questions from API: {e}")
            print("Using local backup questions instead.")
            return self.get_local_questions()

    def play(self):
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/{self.num_questions}:")
            question.display()
            
            while True:
                user_answer = input("Enter your answer (1-4) or 'q' to quit: ")
                
                if user_answer.lower() == 'q':
                    print("Quiz terminated. Thank you for playing!")
                    return
                
                if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                    user_answer = question.options[int(user_answer) - 1]
                    if question.is_correct(user_answer):
                        print("✓ Correct!")
                        self.score += 1
                    else:
                        print(f"✗ Wrong. The correct answer was: {question.correct_answer}")
                    break
                else:
                    print("Invalid input. Please enter a number from 1 to 4.")

            print(f"Current score: {self.score}/{i}")

        print(f"\nQuiz complete! Your final score is: {self.score}/{self.num_questions}")
        self.provide_feedback()

    def provide_feedback(self):
        percentage = (self.score / self.num_questions) * 100
        if percentage >= 90:
            print("Excellent! You're a quiz master!")
        elif percentage >= 70:
            print("Great job! You really know your stuff!")
        elif percentage >= 50:
            print("Good effort! Keep learning!")
        else:
            print("Nice try! Practice makes perfect!")

    def get_local_questions(self) -> List[Question]:
        # Extended backup questions in case the API fails
        return [
            Question("What is the capital of France?", "Paris", ["London", "Berlin", "Rome"]),
            Question("Who wrote 'Romeo and Juliet'?", "William Shakespeare", ["Charles Dickens", "J.K. Rowling", "Jane Austen"]),
            Question("Which planet is known as the Red Planet?", "Mars", ["Venus", "Jupiter", "Saturn"]),
            Question("What is the chemical symbol for gold?", "Au", ["Ag", "Fe", "Gd"]),
            Question("Which animal is known as the 'King of the Jungle'?", "Lion", ["Tiger", "Elephant", "Giraffe"]),
            Question("What is the largest ocean on Earth?", "Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]),
            Question("Who painted the Mona Lisa?", "Leonardo da Vinci", ["Pablo Picasso", "Vincent van Gogh", "Michelangelo"]),
            Question("Which country is known as the Land of the Rising Sun?", "Japan", ["China", "Thailand", "Korea"]),
            Question("What is the smallest prime number?", "2", ["0", "1", "3"]),
            Question("Which element has the chemical symbol 'O'?", "Oxygen", ["Gold", "Silver", "Osmium"])
        ]


# Category IDs for the Open Trivia Database API
CATEGORIES = {
    "General Knowledge": 9,
    "Books": 10,
    "Film": 11,
    "Music": 12,
    "Television": 14,
    "Video Games": 15,
    "Board Games": 16,
    "Science & Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27,
    "Vehicles": 28,
    "Comics": 29,
    "Anime & Manga": 31,
    "Cartoons & Animation": 32
}


def display_categories():
    print("Available quiz categories:")
    for i, (name, _) in enumerate(CATEGORIES.items(), 1):
        print(f"{i}. {name}")


def get_topic() -> int:
    display_categories()
    
    while True:
        topic = input("\nPlease select a category by entering the number (1-22): ")
        if topic.isdigit() and 1 <= int(topic) <= len(CATEGORIES):
            category_name = list(CATEGORIES.keys())[int(topic) - 1]
            category_id = list(CATEGORIES.values())[int(topic) - 1]
            print(f"You selected: {category_name}")
            return category_id
        else:
            print("Invalid input. Please select a valid category number.")


def get_num_questions() -> int:
    while True:
        try:
            num_questions = int(input("How many questions would you like? (1-20): "))
            if 1 <= num_questions <= 20:
                return num_questions
            else:
                print("Please enter a number between 1 and 20.")
        except ValueError:
            print("Please enter a valid number.")


def get_difficulty():
    print("\nDifficulty levels:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Mixed (Random)")
    
    while True:
        choice = input("Select difficulty (1-4): ")
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        elif choice == "4":
            return "mixed"
        else:
            print("Invalid input. Please select a valid difficulty level.")


# Main game loop
if __name__ == "__main__":
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("         🎮 ULTIMATE MULTIPLE CHOICE QUIZ GAME 🎮        ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("Answer each question by entering the number of your choice (1-4).")
    print("Let's begin!\n")

    while True:
        num_questions = get_num_questions()
        category = get_topic()
        # Note: Added difficulty option for future enhancement
        # difficulty = get_difficulty()

        game = QuizGame(num_questions, category)
        game.play()

        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if not play_again.startswith('y'):
            break

    print("Thanks for playing! See you next time!")
