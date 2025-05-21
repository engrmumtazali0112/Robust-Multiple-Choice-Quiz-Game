import requests
import random
import json
import datetime
from typing import List, Dict, Optional, Tuple, Any
import uuid

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.quiz import Quiz, Question, QuizSettings, QuizAnswer, QuizResult, QuizRecord, QuizDetails
from app.models.database import DBQuiz, DBQuestion, DBQuestionOption, DBUserAnswer, DBQuizResult

class QuizService:
    """Service to manage quiz functionality"""
    
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
    def create_quiz(cls, settings: QuizSettings, db: Session) -> Quiz:
        """Create a new quiz based on given settings"""
        # Fetch questions from the API
        questions = cls._fetch_questions(settings.num_questions, settings.category)
        
        # Create a new Quiz instance
        quiz = Quiz.create(
            questions=questions,
            category=settings.category,
            num_questions=settings.num_questions
        )
        
        # Store the quiz in the database
        db_quiz = DBQuiz(
            id=quiz.id,
            category=settings.category,
            num_questions=settings.num_questions,
            current_score=0
        )
        db.add(db_quiz)
        
        # Store questions and options in the database
        for question in quiz.questions:
            db_question = DBQuestion(
                id=question.id,
                quiz_id=quiz.id,
                question=question.question,
                correct_answer=question.correct_answer
            )
            db.add(db_question)
            
            for option in question.options:
                db_option = DBQuestionOption(
                    id=option.id,
                    question_id=question.id,
                    text=option.text
                )
                db.add(db_option)
        
        db.commit()
        
        return quiz
    
    @classmethod
    def get_quiz(cls, quiz_id: str, db: Session) -> Quiz:
        """Get a quiz by ID from the database"""
        # Query the database for the quiz
        db_quiz = db.query(DBQuiz).filter(DBQuiz.id == quiz_id).first()
        if not db_quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        
        # Get the questions for this quiz
        db_questions = db.query(DBQuestion).filter(DBQuestion.quiz_id == quiz_id).all()
        
        # Create a Quiz object
        questions = []
        for db_question in db_questions:
            # Get options for this question
            db_options = db.query(DBQuestionOption).filter(
                DBQuestionOption.question_id == db_question.id
            ).all()
            
            # Create options
            options = [
                {"id": opt.id, "text": opt.text}
                for opt in db_options
            ]
            
            # Check if user has answered this question
            db_answer = db.query(DBUserAnswer).filter(
                DBUserAnswer.question_id == db_question.id
            ).first()
            
            user_answer = None
            is_correct = None
            if db_answer:
                # Get the selected option text
                selected_option = db.query(DBQuestionOption).filter(
                    DBQuestionOption.id == db_answer.selected_option_id
                ).first()
                if selected_option:
                    user_answer = selected_option.text
                    is_correct = db_answer.is_correct
            
            # Create Question object
            from app.models.quiz import QuestionOption
            question = Question(
                id=db_question.id,
                question=db_question.question,
                options=[QuestionOption(id=opt["id"], text=opt["text"]) for opt in options],
                correct_answer=db_question.correct_answer,
                user_answer=user_answer,
                is_correct=is_correct
            )
            questions.append(question)
        
        # Create and return Quiz object
        return Quiz(
            id=db_quiz.id,
            questions=questions,
            category=db_quiz.category,
            num_questions=db_quiz.num_questions,
            current_score=db_quiz.current_score
        )
    
    @classmethod
    def submit_answer(cls, quiz_id: str, answer: QuizAnswer, db: Session) -> Tuple[bool, Optional[str]]:
        """Submit an answer to a quiz question"""
        # Get the quiz from the database
        db_quiz = db.query(DBQuiz).filter(DBQuiz.id == quiz_id).first()
        if not db_quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        
        # Get the question
        db_question = db.query(DBQuestion).filter(DBQuestion.id == answer.question_id).first()
        if not db_question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        # Get the selected option
        db_option = db.query(DBQuestionOption).filter(DBQuestionOption.id == answer.selected_option_id).first()
        if not db_option:
            raise HTTPException(status_code=404, detail="Option not found")
        
        # Check if answer is correct
        is_correct = db_option.text == db_question.correct_answer
        
        # Store the user's answer
        db_answer = db.query(DBUserAnswer).filter(
            DBUserAnswer.question_id == answer.question_id
        ).first()
        
        if db_answer:
            # Update existing answer
            db_answer.selected_option_id = answer.selected_option_id
            db_answer.is_correct = is_correct
        else:
            # Create new answer
            db_answer = DBUserAnswer(
                question_id=answer.question_id,
                selected_option_id=answer.selected_option_id,
                is_correct=is_correct
            )
            db.add(db_answer)
        
        # Update quiz score if correct
        if is_correct:
            db_quiz.current_score += 1
        
        db.commit()
        
        return is_correct, db_question.correct_answer
    
    @classmethod
    def get_quiz_result(cls, quiz_id: str, db: Session) -> QuizResult:
        """Get the result for a completed quiz"""
        # Get the quiz from the database
        db_quiz = db.query(DBQuiz).filter(DBQuiz.id == quiz_id).first()
        if not db_quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        
        # Calculate percentage
        percentage = (db_quiz.current_score / db_quiz.num_questions) * 100
        
        # Generate feedback based on percentage
        feedback = cls._generate_feedback(percentage)
        
        # Check if result already exists
        db_result = db.query(DBQuizResult).filter(DBQuizResult.quiz_id == quiz_id).first()
        
        if not db_result:
            # Create new result
            db_result = DBQuizResult(
                quiz_id=quiz_id,
                score=db_quiz.current_score,
                total_questions=db_quiz.num_questions,
                percentage=percentage,
                feedback=feedback
            )
            db.add(db_result)
            db.commit()
        
        # Create and return result object
        return QuizResult(
            quiz_id=quiz_id,
            score=db_quiz.current_score,
            total_questions=db_quiz.num_questions,
            percentage=percentage,
            feedback=feedback
        )
    
    @classmethod
    def get_quiz_records(cls, db: Session) -> List[QuizRecord]:
        """Get all quiz records from the database"""
        try:
            # Get all quiz results from the database
            db_results = db.query(DBQuizResult, DBQuiz).join(
                DBQuiz, DBQuizResult.quiz_id == DBQuiz.id
            ).order_by(DBQuizResult.created_at.desc()).all()
            
            # Convert to QuizRecord objects
            records = []
            for result, quiz in db_results:
                record = QuizRecord(
                    quiz_id=result.quiz_id,
                    category=quiz.category,
                    score=result.score,
                    total_questions=result.total_questions,  # This is the field used in the template
                    percentage=result.percentage,
                    date_completed=result.created_at
                )
                records.append(record)
            
            return records
        except Exception as e:
            print(f"Error fetching quiz records: {e}")
            return []
    @classmethod
    def get_quiz_details(cls, quiz_id: str, db: Session) -> QuizDetails:
        """Get detailed information about a completed quiz"""
        # Get the quiz and result from the database
        db_result = db.query(DBQuizResult).filter(DBQuizResult.quiz_id == quiz_id).first()
        if not db_result:
            raise HTTPException(status_code=404, detail="Quiz record not found")
        
        db_quiz = db.query(DBQuiz).filter(DBQuiz.id == quiz_id).first()
        if not db_quiz:
            raise HTTPException(status_code=404, detail="Quiz not found")
        
        # Get category name
        category_name = next((name for name, id in cls.CATEGORIES.items() if id == db_quiz.category), "Unknown")
        
        # Get questions with options and answers
        questions_details = []
        db_questions = db.query(DBQuestion).filter(DBQuestion.quiz_id == quiz_id).all()
        
        for db_question in db_questions:
            # Get options
            db_options = db.query(DBQuestionOption).filter(
                DBQuestionOption.question_id == db_question.id
            ).all()
            
            # Get user answer
            db_answer = db.query(DBUserAnswer).filter(
                DBUserAnswer.question_id == db_question.id
            ).first()
            
            user_answer = None
            if db_answer:
                selected_option = db.query(DBQuestionOption).filter(
                    DBQuestionOption.id == db_answer.selected_option_id
                ).first()
                if selected_option:
                    user_answer = selected_option.text
            
            # Map options with selection and correctness info
            options_details = []
            for option in db_options:
                options_details.append({
                    "id": option.id,
                    "text": option.text,
                    "is_correct": option.text == db_question.correct_answer,
                    "is_selected": option.text == user_answer if user_answer else False
                })
            
            questions_details.append({
                "id": db_question.id,
                "question": db_question.question,
                "correct_answer": db_question.correct_answer,
                "user_answer": user_answer,
                "is_correct": db_answer.is_correct if db_answer else None,
                "options": options_details
            })
        
        # Create and return quiz details object
        return QuizDetails(
            quiz_id=quiz_id,
            category=db_quiz.category,
            category_name=category_name,
            score=db_result.score,
            total_questions=db_result.total_questions,
            percentage=db_result.percentage,
            feedback=db_result.feedback,
            date_completed=db_result.created_at,
            questions=questions_details
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