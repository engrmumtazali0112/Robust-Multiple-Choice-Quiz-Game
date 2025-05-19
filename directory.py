import os

# Base directory
base_dir = "quiz_app"

# Directory structure to create
dirs = [
    base_dir,
    os.path.join(base_dir, "app"),
    os.path.join(base_dir, "app", "api"),
    os.path.join(base_dir, "app", "models"),
    os.path.join(base_dir, "app", "services"),
    os.path.join(base_dir, "app", "static"),
    os.path.join(base_dir, "app", "static", "css"),
    os.path.join(base_dir, "app", "static", "js"),
    os.path.join(base_dir, "templates"),
]

# Files to create (relative to base_dir)
files = [
    "main.py",
    "requirements.txt",
    os.path.join("app", "__init__.py"),
    os.path.join("app", "api", "__init__.py"),
    os.path.join("app", "api", "quiz_routes.py"),
    os.path.join("app", "models", "__init__.py"),
    os.path.join("app", "models", "quiz.py"),
    os.path.join("app", "services", "__init__.py"),
    os.path.join("app", "services", "quiz_service.py"),
    os.path.join("app", "static", "css", "style.css"),
    os.path.join("app", "static", "js", "main.js"),
    os.path.join("templates", "base.html"),
    os.path.join("templates", "index.html"),
    os.path.join("templates", "quiz.html"),
]

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create empty files
for f in files:
    file_path = os.path.join(base_dir, f)
    if not os.path.exists(file_path):
        with open(file_path, "w") as fp:
            pass  # Create empty file

print("Directory structure and files created successfully.")
