<div align="center">

# 🎮 Robust Multiple Choice Quiz Game 🎮

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.28+-brightgreen?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![Open Trivia DB](https://img.shields.io/badge/Open_Trivia_DB-API-orange?style=for-the-badge)
![Error Handling](https://img.shields.io/badge/Error_Handling-Robust-red?style=for-the-badge)

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmZrcmFvc2JvODlwaHRmYm9mZnJ5aXNlbGc2MHkyN2o1NDI3N3M0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCScwdMAohPCq76/giphy.gif" width="400" alt="Quiz Animation">
</p>

A robust command-line and web-based quiz game with PostgreSQL database integration, designed to deliver engaging multiple-choice questions from various categories with comprehensive data persistence and analytics.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Version](https://img.shields.io/badge/version-2.0.0-blue)

</div>

## 📋 Description
https://github.com/engrmumtazali0112/Robust-Multiple-Choice-Quiz-Game.git

This comprehensive quiz game system combines an interactive command-line interface with a modern FastAPI web application, featuring PostgreSQL database integration for persistent data storage, user management, and detailed quiz analytics.

## ✨ Key Features

- 🐍 **Python-Powered**: Clean, efficient core logic and game functionality
- 🌐 **API Integration**: Dynamically fetches quiz questions from Open Trivia Database
- 🔄 **Randomization**: Ensures the order of answers is randomized for each question
- ⚠️ **Error Handling**: Seamlessly provides local questions if the API is unavailable
- 🎯 **Multiple Categories**: Choose from 22+ different quiz categories
- 👤 **User-Friendly Design**: Simple and intuitive multiple-choice format
- 📈 **Performance Feedback**: Receive personalized feedback based on your score
- 🗄️ **Database Integration**: PostgreSQL backend for data persistence and user tracking
- 🔍 **Quiz Explorer**: Advanced CLI tool for database management and statistics
- 🌐 **Web Interface**: FastAPI-powered web application with RESTful endpoints
- 📊 **Analytics Dashboard**: Comprehensive quiz statistics and performance tracking

## 🗄️ Database Architecture

The application uses PostgreSQL as its primary database with a well-structured schema designed for scalability and performance.

### Database Tables

| Table | Description |
|-------|-------------|
| `users` | User account information and authentication data |
| `quizzes` | Quiz metadata including categories and creation timestamps |
| `questions` | Individual quiz questions with multiple choice options |
| `question_options` | Answer choices for each question |
| `user_answers` | User responses and answer tracking |
| `quiz_results` | Quiz completion records with scores and performance metrics |
| `quiz_records` | Detailed quiz attempt history |

### Quiz Explorer (`quiz_explorer.py`)

**Advanced Database Management Tool**
Interactive command-line interface for comprehensive quiz database exploration and management.

#### Features:

| ![Quiz Listing](https://github.com/user-attachments/assets/51983236-3071-438d-ace0-2cd01547c489) | ![Detailed Views](https://github.com/user-attachments/assets/3c4a4ada-4aae-4a85-a999-f1847396b84a) | ![Results Analysis](https://github.com/user-attachments/assets/cca93842-d900-4a52-a4c1-cb887993d4ea) |
| --- | --- | --- |
| **📋 Quiz Listing**: View all available quizzes with categories and metadata in a structured table format | **🔍 Detailed Views**: Examine specific quiz details using quiz IDs with comprehensive information display | **📊 Results Analysis**: Comprehensive quiz results with scoring and percentages for performance tracking |

| ![Statistics Dashboard](https://github.com/user-attachments/assets/b15174b1-20cf-4281-b081-3d3c3256ce1b) | ![Real-time Data](https://github.com/user-attachments/assets/22ab097f-88de-44fd-a50e-4b0dbd1303b7) |
| --- | --- |
| **📈 Statistics Dashboard**: Category-wise performance analytics and trends with average score calculations | **⚡ Real-time Data**: Live database connectivity with up-to-date information and instant data retrieval |

#### Available Operations:
1. **List All Quizzes** - Display complete quiz inventory
2. **View Quiz Details** - Detailed quiz information (requires quiz ID)
3. **List Quiz Results** - Performance metrics and completion data
4. **View Quiz Statistics** - Category-wise analytics and average scores
5. **Exit** - Clean application termination

### Database Console (`quiz_db#`)

**PostgreSQL Command Interface**
Direct database access through PostgreSQL command-line interface for advanced operations.

#### Key Commands:

| ![Database Relations](https://github.com/user-attachments/assets/49393e1d-b4d2-4498-ad4d-b17c46e493c2) | ![Quiz Results](https://github.com/user-attachments/assets/949792bf-4cc2-463d-a6d0-6e76f144d112) |
| --- | --- |
| **`\d`** - List all database relations and tables with schema information | **`SELECT * FROM quiz_results;`** - View quiz completion records with detailed performance data |

#### Additional Commands:
- **`\l`** - List all available databases
- **`SELECT * FROM quiz_statistics;`** - Access performance analytics

## 🎥 Demo
### Quiz Game Features

<details>
<summary>Click to view Demo</summary>

| ![Quiz Question Screen](https://github.com/user-attachments/assets/8f2ad6f3-77b2-4ece-acd2-43564b9b2fdd) | ![Answer Selection](https://github.com/user-attachments/assets/5cbb0fc4-8e4e-496a-a0cf-0fd4be3e751c) | ![Score Summary](https://github.com/user-attachments/assets/2439b7c5-13bb-49e9-ad0b-1a2245e37e34) | 
| --- | --- | --- |
| **Quiz Question Screen**: Interactive multiple-choice question interface where questions are displayed and randomized answer options are provided. | **Answer Selection**: Users select an answer from the options provided in the quiz interface. | **Score Summary**: Final score feedback based on the user's correct answers, including a percentage and performance summary. |

| ![Game Feedback](https://github.com/user-attachments/assets/c1e981ba-a33d-41d9-9ac3-13aa2ae6c4ee) | ![Gameplay Example](https://github.com/user-attachments/assets/2c5bee0f-9cda-41d0-a913-bf93e502a9f2) | ![User Result](https://github.com/user-attachments/assets/f17b26a0-f6aa-4095-be1f-6ffc898676b8) |
| --- | --- | --- |
| **Game Feedback**: Visual feedback provided after each question or at the end of the game, summarizing the user's performance. | **Gameplay Example**: An example of the user's progress during the quiz, showing how the system updates after each response. | **User Result**: The results page displaying the final score and detailed analysis based on the user's answers. |

| ![Quiz End Screen](https://github.com/user-attachments/assets/ac253834-c221-4fa1-b5c7-8d40a6e47068) | 
| --- | --- |
| **Quiz End Screen**: The concluding screen showing total score and an option to restart or finish the quiz.

</details>

## 🚀 Installation

### Prerequisites
- Python 3.12+
- PostgreSQL 13+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/engrmumtazali0112/Robust-Multiple-Choice-Quiz-Game
   ```

2. **Navigate to the project directory**
   ```bash
   cd Robust-Multiple-Choice-Quiz-Game
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   # Create PostgreSQL database
   createdb quiz_db
   
   # Run database migrations (if using Alembic)
   alembic upgrade head
   ```

5. **Environment Configuration**
   ```bash
   # Create .env file with database credentials
   DATABASE_URL=postgresql://username:password@localhost:5432/quiz_db
   ```

## 🧩 Project Structure

```
quiz_app/
├── main.py                  # FastAPI application entry point
├── quiz_explorer.py         # Database management CLI tool
├── requirements.txt         # Project dependencies
├── .env                     # Environment variables
├── alembic.ini             # Database migration configuration
├── app/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py    # Database connection management
│   │   └── models.py        # SQLAlchemy models
│   ├── api/
│   │   ├── __init__.py
│   │   └── quiz_routes.py   # API endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   └── quiz.py          # Pydantic models
│   ├── services/
│   │   ├── __init__.py
│   │   └── quiz_service.py  # Business logic
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── templates/
│   ├── base.html
│   ├── index.html
│   └── quiz.html
└── migrations/              # Alembic database migrations
    └── versions/
```

## 🎮 How to Play

### Command Line Interface
1. **Run the CLI game**
   ```bash
   python main.py
   ```

2. **Database Explorer**
   ```bash
   python quiz_explorer.py
   ```

### Web Interface
1. **Start the FastAPI server**
   ```bash
   cd quiz_app
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the web interface**
   ```
   http://localhost:8000
   ```

### Game Flow
1. **Select the number of questions** (1-20)
2. **Choose a category** from the available options
3. **Answer each question** by entering the number of your choice (1-4)
4. **Receive feedback** on your performance
5. **View detailed analytics** through the explorer tool

## 📊 Available Categories

| Category ID | Name                  | Category ID | Name                  |
|------------|------------------------|------------|------------------------|
| 9          | General Knowledge      | 21         | Sports                 |
| 10         | Books                  | 22         | Geography              |
| 11         | Film                   | 23         | History                |
| 12         | Music                  | 24         | Politics               |
| 14         | Television             | 25         | Art                    |
| 15         | Video Games            | 26         | Celebrities            |
| 16         | Board Games            | 27         | Animals                |
| 17         | Science & Nature       | 28         | Vehicles               |
| 18         | Computers              | 29         | Comics                 |
| 19         | Mathematics            | 31         | Anime & Manga          |
| 20         | Mythology              | 32         | Cartoons & Animation   |

## 🔧 API Endpoints

### Quiz Management
- `GET /api/quizzes` - List all available quizzes
- `GET /api/quizzes/{quiz_id}` - Get specific quiz details
- `POST /api/quizzes` - Create a new quiz
- `GET /api/quizzes/{quiz_id}/result` - Get quiz results

### User Management
- `POST /api/users` - Create new user account
- `GET /api/users/{user_id}/stats` - Get user statistics

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/engrmumtazali0112/Robust-Multiple-Choice-Quiz-Game/issues).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgements

A big thanks to [@EcodeCamp](https://github.com/EcodeCamp) for inspiring this project and encouraging developers to enhance their skills through practical coding challenges.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=36BCF7&center=true&vCenter=true&width=435&lines=Made+with+%E2%9D%A4%EF%B8%8F+by+Mumtaz+Ali" alt="Made with love by Mumtaz Ali" />
</div>

<p align="center">
  <a href="mailto:engrmumtazali01@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/mumtazali12/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.instagram.com/its_maliyzi?igsh=MWR1Y2x1a2xpazBpOA==" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
  </a>
  <a href="https://www.hackerrank.com/profile/engrmumtazali01" target="_blank">
    <img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white" alt="HackerRank" />
  </a>
  <a href="https://github.com/engrmumtazali0112" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---

<div align="center">
    <p>⭐ Star this repo if you found it useful! ⭐</p>
    <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="Built with Love">
    <p>
        <img src="https://media.giphy.com/media/l378BzHA5FwWFXVSg/giphy.gif" width="30" />
        Happy Coding!
        <img src="https://media.giphy.com/media/l378BzHA5FwWFXVSg/giphy.gif" width="30" />
    </p>
</div>
