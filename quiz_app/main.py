from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from typing import Optional, List

from app.models.quiz import QuizSettings
from app.services.quiz_service import QuizService
from app.api.quiz_routes import router as quiz_router

app = FastAPI(title="Quiz Game API")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Include API routes
app.include_router(quiz_router, prefix="/api")

# Frontend routes
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Render the home page with quiz setup form"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/quiz", response_class=HTMLResponse)
async def quiz_page(request: Request, quiz_id: Optional[str] = None):
    """Render the quiz page"""
    if not quiz_id:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("quiz.html", {"request": request, "quiz_id": quiz_id})

@app.get("/records")
async def records(request: Request):
    quiz_records = QuizService.get_quiz_records()
    categories = QuizService.get_categories()
    
    # Create an inverted dictionary for easy lookup (id -> name)
    categories_by_id = {id: name for name, id in categories.items()}
    
    return templates.TemplateResponse(
        "records.html", 
        {"request": request, "quiz_records": quiz_records, "categories": categories, "categories_by_id": categories_by_id}
    )
@app.get("/quiz-details", response_class=HTMLResponse)
async def quiz_details(request: Request, quiz_id: Optional[str] = None):
    """Render the quiz details page"""
    if not quiz_id:
        return RedirectResponse(url="/records")
    return templates.TemplateResponse("quiz_details.html", {"request": request, "quiz_id": quiz_id})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
