from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from typing import Optional
from sqlalchemy.orm import Session

from app.models.quiz import QuizSettings
from app.services.quiz_service import QuizService
from app.api.quiz_routes import router as quiz_router
from app.database import get_db

app = FastAPI(title="Quiz Game API")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Include API routes
app.include_router(quiz_router, prefix="/api")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the home page with quiz setup form"""
    categories = QuizService.get_categories()
    return templates.TemplateResponse("index.html", {"request": request, "categories": categories})


@app.delete("/delete-quiz-record/{quiz_id}")
async def delete_quiz_record(quiz_id: str, db: Session = Depends(get_db)):
    success = QuizService.delete_quiz_record(quiz_id, db)
    if success:
        return {"status": "success", "message": "Quiz record deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete quiz record")


@app.get("/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request, quiz_id: Optional[str] = None):
    """Render the quiz page"""
    if not quiz_id:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("quiz.html", {"request": request, "quiz_id": quiz_id})


@app.get("/records", response_class=HTMLResponse)
async def records(request: Request, db: Session = Depends(get_db)):
    quiz_records = QuizService.get_quiz_records(db)
    categories = QuizService.get_categories()
    categories_by_id = {id: name for name, id in categories.items()}
    return templates.TemplateResponse(
        "records.html",
        {
            "request": request,
            "quiz_records": quiz_records,
            "categories": categories,
            "categories_by_id": categories_by_id,
        },
    )


@app.get("/quiz-details", response_class=HTMLResponse)
async def quiz_details(request: Request, quiz_id: Optional[str] = None):
    """Render the quiz details page"""
    if not quiz_id:
        return RedirectResponse(url="/records")
    return templates.TemplateResponse("quiz_details.html", {"request": request, "quiz_id": quiz_id})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
