from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List, Any

from app.models.quiz import QuizSettings, QuizAnswer, QuizResult, QuizRecord, QuizDetails
from app.services.quiz_service import QuizService

router = APIRouter()

@router.get("/categories")
async def get_categories() -> Dict[str, int]:
    """Get all available quiz categories"""
    return QuizService.get_categories()

@router.post("/quizzes")
async def create_quiz(settings: QuizSettings) -> Dict[str, str]:
    """Create a new quiz"""
    quiz = QuizService.create_quiz(settings)
    return {"quiz_id": quiz.id}

@router.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id: str) -> Dict[str, Any]:
    """Get a quiz by ID"""
    quiz = QuizService.get_quiz(quiz_id)
    
    # Convert to dict and only send necessary information to frontend
    return {
        "quiz_id": quiz.id,
        "category": quiz.category,
        "num_questions": quiz.num_questions,
        "current_score": quiz.current_score,
        "questions": [
            {
                "id": q.id,
                "question": q.question,
                "options": [{"id": opt.id, "text": opt.text} for opt in q.options]
            }
            for q in quiz.questions
        ]
    }

@router.post("/quizzes/{quiz_id}/answer")
async def submit_answer(quiz_id: str, answer: QuizAnswer) -> Dict[str, Any]:
    """Submit an answer to a quiz question"""
    is_correct, correct_answer = QuizService.submit_answer(quiz_id, answer)
    return {"is_correct": is_correct, "correct_answer": correct_answer}

@router.get("/quizzes/{quiz_id}/result")
async def get_quiz_result(quiz_id: str) -> QuizResult:
    """Get the result for a completed quiz"""
    return QuizService.get_quiz_result(quiz_id)

@router.get("/quizzes/{quiz_id}/details")
async def get_quiz_details(quiz_id: str) -> QuizDetails:
    """Get detailed information about a completed quiz"""
    return QuizService.get_quiz_details(quiz_id)


@router.get("/records")
async def get_records() -> List[QuizRecord]:
    """Get all quiz records"""
    return QuizService.get_quiz_records()
