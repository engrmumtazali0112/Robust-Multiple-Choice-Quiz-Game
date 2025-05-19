from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database import Base

class DBQuiz(Base):
    """Database model for Quiz"""
    __tablename__ = "quizzes"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    category = Column(Integer, index=True)
    num_questions = Column(Integer)
    current_score = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(String, index=True, nullable=True)  # Optional user ID for authentication

    # Relationships
    questions = relationship("DBQuestion", back_populates="quiz", cascade="all, delete-orphan")
    results = relationship("DBQuizResult", back_populates="quiz", cascade="all, delete-orphan")

class DBQuestion(Base):
    """Database model for Question"""
    __tablename__ = "questions"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    quiz_id = Column(String, ForeignKey("quizzes.id"))
    question = Column(Text)
    correct_answer = Column(String)

    # Relationships
    quiz = relationship("DBQuiz", back_populates="questions")
    options = relationship("DBQuestionOption", back_populates="question", cascade="all, delete-orphan")
    answers = relationship("DBUserAnswer", back_populates="question", cascade="all, delete-orphan")

class DBQuestionOption(Base):
    """Database model for Question Option"""
    __tablename__ = "question_options"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    question_id = Column(String, ForeignKey("questions.id"))
    text = Column(String)

    # Relationships
    question = relationship("DBQuestion", back_populates="options")

class DBUserAnswer(Base):
    """Database model for User Answers"""
    __tablename__ = "user_answers"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    question_id = Column(String, ForeignKey("questions.id"))
    selected_option_id = Column(String, ForeignKey("question_options.id"))
    is_correct = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(String, index=True, nullable=True)  # Optional user ID for authentication

    # Relationships
    question = relationship("DBQuestion", back_populates="answers")
    selected_option = relationship("DBQuestionOption")

class DBQuizResult(Base):
    """Database model for Quiz Results"""
    __tablename__ = "quiz_results"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    quiz_id = Column(String, ForeignKey("quizzes.id"))
    score = Column(Integer)
    total_questions = Column(Integer)
    percentage = Column(Float)
    feedback = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(String, index=True, nullable=True)  # Optional user ID for authentication

    # Relationships
    quiz = relationship("DBQuiz", back_populates="results")