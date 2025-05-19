import requests
import random
import json
from typing import List, Dict, Optional, Tuple
import uuid

from fastapi import HTTPException
from app.models.quiz import Quiz, Question, QuizSettings, QuizAnswer, QuizResult

class QuizService:
    """Service to manage quiz functionality"""
    
    # Store quizzes in memory (would use a database in production)
    _quizzes = {}
    
    # Define the OpenTrivia Database API URL
    TRIVIA_API_URL = "https://opentdb.com/api.php"
    
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
    
    @classmethod
    def get_categories(cls) -> Dict[str, int]:
        """Get all available quiz categories"""
        return cls.CATEGORIES
    
    @classmethod
    def create_quiz(cls, settings: QuizSettings) -> Quiz:
        """Create a new quiz based on given settings"""
        # Fetch questions from the API
        questions = cls._fetch_questions(settings.num_questions, settings.category)
        
        # Create a new Quiz instance
        quiz = Quiz.create(
            questions=questions,
            category=settings.category,
            num_questions=settings.num_questions
        )
        
        # Store the quiz in our in-memory data store
        cls._quizzes[quiz.id] = quiz
        
        return quiz
    
    @classmethod
    def get_quiz(cls, quiz_id: str) -> Quiz:
        """Get a quiz by ID"""
        if quiz_id not in cls._quizzes:
            raise HTTPException(status_code=404, detail="Quiz not found")
        return cls._quizzes[quiz_id]
    
    @classmethod
    def submit_answer(cls, quiz_id: str, answer: QuizAnswer) -> Tuple[bool, Optional[str]]:
        """Submit an answer to a quiz question"""
        quiz = cls.get_quiz(quiz_id)
        
        # Find the question
        question = next((q for q in quiz.questions if q.id == answer.question_id), None)
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Find the selected option
        selected_option = next((opt for opt in question.options if opt.id == answer.selected_option_id), None)
        if not selected_option:
            raise HTTPException(status_code=404, detail="Option not found")
        
        # Check if answer is correct
        is_correct = selected_option.text == question.correct_answer
        
        if is_correct:
            # Update the score
            quiz.current_score += 1
            
        # Update the quiz in our store
        cls._quizzes[quiz_id] = quiz
        
        return is_correct, question.correct_answer
    
    @classmethod
    def get_quiz_result(cls, quiz_id: str) -> QuizResult:
        """Get the result for a completed quiz"""
        quiz = cls.get_quiz(quiz_id)
        
        # Calculate percentage
        percentage = (quiz.current_score / quiz.num_questions) * 100
        
        # Generate feedback based on percentage
        feedback = cls._generate_feedback(percentage)
        
        return QuizResult(
            quiz_id=quiz_id,
            score=quiz.current_score,
            total_questions=quiz.num_questions,
            percentage=percentage,
            feedback=feedback
        )
    
    @classmethod
    def _fetch_questions(cls, num_questions: int, category: int) -> List[Question]:
        """Fetch questions from the API or use backup questions if API fails"""
        try:
            url = f"{cls.TRIVIA_API_URL}?amount={num_questions}&category={category}&type=multiple"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data['response_code'] == 0:
                return [Question.from_api(q) for q in data['results']]
            else:
                print(f"API Error: {data.get('response_message', 'Unknown error')}")
                return cls._get_local_questions(num_questions)
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            print(f"Error fetching questions from API: {e}")
            print("Using local backup questions instead.")
            return cls._get_local_questions(num_questions)
    
    @classmethod
    def _get_local_questions(cls, num_questions: int) -> List[Question]:
        """Get local backup questions"""
        # Define backup questions as dictionaries in the format expected by Question.from_api
        backup_questions = [
            {
                "question": "What is the capital of France?",
                "correct_answer": "Paris",
                "incorrect_answers": ["London", "Berlin", "Rome"]
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "correct_answer": "William Shakespeare",
                "incorrect_answers": ["Charles Dickens", "J.K. Rowling", "Jane Austen"]
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "correct_answer": "Mars", 
                "incorrect_answers": ["Venus", "Jupiter", "Saturn"]
            },
            {
                "question": "What is the chemical symbol for gold?",
                "correct_answer": "Au",
                "incorrect_answers": ["Ag", "Fe", "Gd"]
            },
            {
                "question": "Which animal is known as the 'King of the Jungle'?",
                "correct_answer": "Lion",
                "incorrect_answers": ["Tiger", "Elephant", "Giraffe"]
            },
            {
                "question": "What is the largest ocean on Earth?",
                "correct_answer": "Pacific Ocean",
                "incorrect_answers": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"]
            },
            {
                "question": "Who painted the Mona Lisa?",
                "correct_answer": "Leonardo da Vinci",
                "incorrect_answers": ["Pablo Picasso", "Vincent van Gogh", "Michelangelo"]
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "correct_answer": "Japan",
                "incorrect_answers": ["China", "Thailand", "Korea"]
            },
            {
                "question": "What is the smallest prime number?",
                "correct_answer": "2",
                "incorrect_answers": ["0", "1", "3"]
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "correct_answer": "Oxygen",
                "incorrect_answers": ["Gold", "Silver", "Osmium"]
            }
        ]
        
        # Shuffle and limit to requested number
        random.shuffle(backup_questions)
        backup_questions = backup_questions[:num_questions]
        
        # Convert to Question objects
        return [Question.from_api(q) for q in backup_questions]
    
    @staticmethod
    def _generate_feedback(percentage: float) -> str:
        """Generate feedback based on percentage score"""
        if percentage >= 90:
            return "Excellent! You're a quiz master!"
        elif percentage >= 70:
            return "Great job! You really know your stuff!"
        elif percentage >= 50:
            return "Good effort! Keep learning!"
        else:
            return "Nice try! Practice makes perfect!"