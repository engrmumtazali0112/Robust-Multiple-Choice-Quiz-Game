from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import uuid
import datetime
import html
import random


class QuestionOption(BaseModel):
    """Model for a single answer option"""
    id: str
    text: str


class Question(BaseModel):
    """Model for a single quiz question"""
    id: str
    question: str
    options: List[QuestionOption]
    correct_answer: str
    user_answer: Optional[str] = None
    is_correct: Optional[bool] = None
    
    @classmethod
    def from_api(cls, raw_question: Dict[str, Any]) -> 'Question':
        """Create a Question object from API response data"""
        # Clean and unescape HTML entities
        question_text = html.unescape(raw_question['question'])
        correct_answer = html.unescape(raw_question['correct_answer'])
        
        # Process all options
        all_options = [html.unescape(ans) for ans in raw_question['incorrect_answers']]
        all_options.append(correct_answer)
        
        # Randomize the order of options
        random.shuffle(all_options)
        
        # Create option objects with unique IDs
        options = []
        for option_text in all_options:
            option_id = str(uuid.uuid4())
            options.append(QuestionOption(id=option_id, text=option_text))
            
        return cls(
            id=str(uuid.uuid4()),
            question=question_text,
            options=options,
            correct_answer=correct_answer
        )


class Quiz(BaseModel):
    """Model for an entire quiz"""
    id: str
    questions: List[Question]
    category: int
    num_questions: int
    current_score: int = 0
    
    @classmethod
    def create(cls, questions: List[Question], category: int, num_questions: int) -> 'Quiz':
        """Create a new Quiz instance"""
        return cls(
            id=str(uuid.uuid4()),
            questions=questions,
            category=category,
            num_questions=num_questions
        )


class QuizSettings(BaseModel):
    """Model for quiz configuration settings"""
    num_questions: int = Field(default=10, ge=1, le=20)
    category: int = Field(default=9)  # Default to General Knowledge


class QuizAnswer(BaseModel):
    """Model for an answer submission"""
    question_id: str
    selected_option_id: str


class QuizResult(BaseModel):
    """Model for quiz results"""
    quiz_id: str
    score: int
    total_questions: int
    percentage: float
    feedback: str


class QuizRecord(BaseModel):
    """Model for storing a completed quiz record"""
    quiz_id: str
    category: int
    score: int
    total_questions: int
    percentage: float
    date_completed: datetime.datetime


class QuizDetails(BaseModel):
    """Model for detailed quiz information"""
    quiz_id: str
    category: int
    category_name: str
    score: int
    total_questions: int
    percentage: float
    feedback: str
    date_completed: datetime.datetime
    questions: List[Dict[str, Any]]