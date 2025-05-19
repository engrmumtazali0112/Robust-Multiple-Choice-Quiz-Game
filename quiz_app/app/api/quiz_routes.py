from fastapi import APIRouter, HTTPException, Depends
from typing import Dict, List, Any

from app.models.quiz import QuizSettings, Quiz, QuizAnswer, QuizResult
from app.services.quiz_service import QuizService

router = APIRouter(tags=["quiz"])

@router.get("/categories")
async def get_categories() -> Dict[str, int]:
    """Get all available quiz categories"""
    return QuizService.get_categories()

@router.post("/quizzes", response_model=Dict[str, Any])
async def create_quiz(settings: QuizSettings) -> Dict[str, Any]:
    """Create a new quiz based on given settings"""
    quiz = QuizService.create_quiz(settings)
    
    # Return a limited version of the quiz to avoid revealing correct answers
    return {
        "quiz_id": quiz.id,
        "category": quiz.category,
        "num_questions": quiz.num_questions,
        "questions": [
            {
                "id": q.id,
                "question": q.question,
                "options": [{"id": opt.id, "text": opt.text} for opt in q.options]
            } for q in quiz.questions
        ],
    }

@router.get("/quizzes/{quiz_id}", response_model=Dict[str, Any])
async def get_quiz(quiz_id: str) -> Dict[str, Any]:
    """Get a quiz by ID"""
    try:
        quiz = QuizService.get_quiz(quiz_id)
        
        # Return a limited version of the quiz to avoid revealing correct answers
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
                } for q in quiz.questions
            ],
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/quizzes/{quiz_id}/answer", response_model=Dict[str, Any])
async def submit_answer(quiz_id: str, answer: QuizAnswer) -> Dict[str, Any]:
    """Submit an answer to a quiz question"""
    try:
        is_correct, correct_answer = QuizService.submit_answer(quiz_id, answer)
        return {
            "is_correct": is_correct,
            "correct_answer": correct_answer
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/quizzes/{quiz_id}/result", response_model=QuizResult)
async def get_quiz_result(quiz_id: str) -> QuizResult:
    """Get the result for a completed quiz"""
    try:
        return QuizService.get_quiz_result(quiz_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))