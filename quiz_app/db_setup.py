"""
Database setup and migration script for Quiz Application
"""
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import alembic.config
import sys

# Add the parent directory to the path so we can import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import our models
from app.database import Base, engine
from app.models.database import DBQuiz, DBQuestion, DBQuestionOption, DBUserAnswer, DBQuizResult

def create_tables():
    """Create all tables defined in the models"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def drop_tables():
    """Drop all tables (dangerous!)"""
    confirm = input("This will drop all tables! Type 'YES' to confirm: ")
    if confirm == "YES":
        print("Dropping all tables...")
        Base.metadata.drop_all(bind=engine)
        print("All tables dropped!")
    else:
        print("Operation cancelled.")

def run_migrations():
    """Run Alembic migrations"""
    print("Running database migrations...")
    alembic_args = [
        '--raiseerr',
        'upgrade', 'head',
    ]
    alembic.config.main(argv=alembic_args)
    print("Migrations completed successfully!")

def create_sample_data():
    """Create some sample data for testing"""
    from sqlalchemy.orm import sessionmaker
    from app.services.quiz_service import QuizService
    from app.models.quiz import QuizSettings
    
    print("Creating sample quiz data...")
    
    # Create a session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Create a sample quiz with general knowledge questions
        settings = QuizSettings(num_questions=5, category=9)
        quiz = QuizService.create_quiz(settings, db)
        
        print(f"Created sample quiz with ID: {quiz.id}")
        
        # Create another sample quiz with science questions
        settings = QuizSettings(num_questions=3, category=17)
        quiz = QuizService.create_quiz(settings, db)
        
        print(f"Created sample quiz with ID: {quiz.id}")
        
        db.commit()
        print("Sample data created successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error creating sample data: {e}")
    finally:
        db.close()

def print_help():
    """Print usage information"""
    print("Quiz App Database Management Tool")
    print("================================")
    print("Usage: python db_setup.py [command]")
    print("\nCommands:")
    print("  create    - Create all database tables")
    print("  drop      - Drop all database tables (destructive!)")
    print("  migrate   - Run database migrations")
    print("  sample    - Create sample data")
    print("  help      - Show this help message")

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Check if DATABASE_URL is set
    if not os.getenv("DATABASE_URL"):
        print("Error: DATABASE_URL environment variable is not set.")
        print("Please create a .env file with DATABASE_URL=sqlite:///./quiz_app.db")
        sys.exit(1)
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == "create":
        create_tables()
    elif command == "drop":
        drop_tables()
    elif command == "migrate":
        run_migrations()
    elif command == "sample":
        create_sample_data()
    elif command == "help":
        print_help()
    else:
        print(f"Unknown command: {command}")
        print_help()
        sys.exit(1)