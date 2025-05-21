import os

# Base directory
base_dir = "quiz_app"

# Directory structure to create
dirs = [
    base_dir,
    # App structure
    os.path.join(base_dir, "app"),
    os.path.join(base_dir, "app", "api"),
    os.path.join(base_dir, "app", "models"),
    os.path.join(base_dir, "app", "services"),
    # Static assets
    os.path.join(base_dir, "app", "static"),
    os.path.join(base_dir, "app", "static", "css"),
    os.path.join(base_dir, "app", "static", "js"),
    os.path.join(base_dir, "app", "static", "img"),
    # Templates
    os.path.join(base_dir, "templates"),
    # Database migrations
    os.path.join(base_dir, "migrations"),
    os.path.join(base_dir, "migrations", "versions"),
]

# Files to create (relative to base_dir)
files = [
    # Root files
    "main.py",
    "requirements.txt",
    "db_setup.py",
    "alembic.ini",
    ".env",
    ".env.example",
    # App files
    os.path.join("app", "__init__.py"),
    os.path.join("app", "database.py"),
    # API
    os.path.join("app", "api", "__init__.py"),
    os.path.join("app", "api", "quiz_routes.py"),
    # Models
    os.path.join("app", "models", "__init__.py"),
    os.path.join("app", "models", "database.py"),
    os.path.join("app", "models", "quiz.py"),
    # Services
    os.path.join("app", "services", "__init__.py"),
    os.path.join("app", "services", "quiz_service.py"),
    # Static assets
    os.path.join("app", "static", "css", "style.css"),
    os.path.join("app", "static", "js", "main.js"),
    # Migrations
    os.path.join("migrations", "env.py"),
    os.path.join("migrations", "script.py.mako"),
    os.path.join("migrations", "versions", "__init__.py"),
    # Templates
    os.path.join("templates", "base.html"),
    os.path.join("templates", "index.html"),
    os.path.join("templates", "quiz.html"),
    os.path.join("templates", "quiz_details.html"),
    os.path.join("templates", "records.html"),
]

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)
    print(f"Created directory: {d}")

# Create empty files
for f in files:
    file_path = os.path.join(base_dir, f)
    if not os.path.exists(file_path):
        with open(file_path, "w") as fp:
            pass  # Create empty file
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")

# Add basic content to requirements.txt
requirements_content = """sqlalchemy>=1.4.0,<2.0.0
psycopg2-binary>=2.9.3
fastapi>=0.100.0
uvicorn>=0.22.0
pydantic>=1.10.0
requests>=2.28.0
python-multipart>=0.0.6
jinja2>=3.1.0
alembic>=1.10.0
"""

with open(os.path.join(base_dir, "requirements.txt"), "w") as f:
    f.write(requirements_content)
    print("Added content to requirements.txt")

# Add sample content to .env.example
env_example_content = """# Database Connection
DATABASE_URL=postgresql://username:password@localhost/quiz_db

# API Settings
TRIVIA_API_URL=https://opentdb.com/api.php

# Application Settings
SECRET_KEY=your_secret_key_here
DEBUG=True
"""

with open(os.path.join(base_dir, ".env.example"), "w") as f:
    f.write(env_example_content)
    print("Added content to .env.example")

print("\nDirectory structure and files created successfully.")
print("\nNext steps:")
print("1. Customize your .env file with your database credentials")
print("2. Run 'pip install -r requirements.txt' to install dependencies")
print("3. Initialize the database with 'python db_setup.py'")
print("4. Run the application with 'uvicorn main:app --reload'")