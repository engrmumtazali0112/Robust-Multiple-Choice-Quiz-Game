<div align="center">

# 🎮 Robust Multiple Choice Quiz Game 🎮

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0+-green?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4+-red?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![Open Trivia DB](https://img.shields.io/badge/Open_Trivia_DB-API-orange?style=for-the-badge)
![Error Handling](https://img.shields.io/badge/Error_Handling-Robust-red?style=for-the-badge)

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmZrcmFvc2JvODlwaHRmYm9mZnJ5aXNlbGc2MHkyN2o1NDI3N3M0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCScwdMAohPCq76/giphy.gif" width="400" alt="Quiz Animation">
</p>

A robust web-based quiz application designed to test your knowledge with multiple-choice questions from various categories. Now with database integration for persistent storage of quiz records and user scores!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Version](https://img.shields.io/badge/version-2.0.0-blue)

</div>

## 📋 Description

This interactive quiz application fetches random questions using the Open Trivia Database API and provides a fallback to local questions if the API is unavailable. Built with FastAPI and SQLAlchemy, the application now includes database functionality for storing quiz results and user profiles. Challenge yourself with questions from more than 20 different categories!

## ✨ Key Features

- 🐍 **Python-Powered**: Clean, efficient core logic and game functionality
- 🌐 **API Integration**: Dynamically fetches quiz questions from Open Trivia Database
- 💾 **Database Storage**: Persistent storage for quiz records, user scores, and profiles
- 🔄 **Randomization**: Ensures the order of answers is randomized for each question
- ⚠️ **Error Handling**: Seamlessly provides local questions if the API is unavailable
- 🎯 **Multiple Categories**: Choose from 22+ different quiz categories
- 🖥️ **Web Interface**: Modern and responsive UI using FastAPI, Jinja2, and CSS
- 📊 **Score History**: Track your progress over time with detailed records
- 📈 **Performance Feedback**: Receive personalized feedback based on your score
- 🔄 **Database Migrations**: Managed with Alembic for easy schema updates

## 🎥 Demo
### Quiz Game Features

<details>
<summary>Click to view Demo</summary>

| ![Quiz Question Screen](https://github.com/user-attachments/assets/8f2ad6f3-77b2-4ece-acd2-43564b9b2fdd) | ![Answer Selection](https://github.com/user-attachments/assets/5cbb0fc4-8e4e-496a-a0cf-0fd4be3e751c) | ![Score Summary](https://github.com/user-attachments/assets/2439b7c5-13bb-49e9-ad0b-1a2245e37e34) | 
| --- | --- | --- |
| **Quiz Question Screen**: Interactive multiple-choice question interface where questions are displayed and randomized answer options are provided. | **Answer Selection**: Users select an answer from the options provided in the quiz interface. | **Score Summary**: Final score feedback based on the user's correct answers, including a percentage and performance summary. |

| ![Game Feedback](https://github.com/user-attachments/assets/c1e981ba-a33d-41d9-9ac3-13aa2ae6c4ee) | ![Gameplay Example](https://github.com/user-attachments/assets/2c5bee0f-9cda-41d0-a913-bf93e502a9f2) | ![User Result](https://github.com/user-attachments/assets/ba52b610-3711-451b-a2fd-3abc46e46780) |
| --- | --- | --- |
| **Game Feedback**: Visual feedback provided after each question or at the end of the game, summarizing the user's performance. | **Gameplay Example**: An example of the user's progress during the quiz, showing how the system updates after each response. | **User Result**: The results page displaying the final score and detailed analysis based on the user's answers. |

| ![Quiz End Screen](https://github.com/user-attachments/assets/ec1891e4-9502-4f27-93f8-b6bf7cb49ad4) | ![Feedback Detail](https://github.com/user-attachments/assets/4b93c578-95ec-4908-b9aa-8137e048f1bc) |
| --- | --- |
| **Quiz End Screen**: The concluding screen showing total score and an option to restart or finish the quiz. | **Feedback Detail**: Provides detailed feedback on each question, helping the user understand the mistakes and correct answers. |

</details>

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/engrmumtazali0112/Robust-Multiple-Choice-Quiz-Game
   ```

2. **Navigate to the project directory**
   ```bash
   cd Robust-Multiple-Choice-Quiz-Game
   ```

3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database connection string and other settings
   ```

6. **Set up the database**
   ```bash
   python db_setup.py
   ```

7. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

## 🧩 Project Structure

```
quiz-app/
├── .env                      # Environment variables (create from .env.example)
├── alembic.ini               # Alembic configuration
├── db_setup.py               # Database setup script
├── main.py                   # FastAPI application entry point
├── requirements.txt          # Python dependencies
│
├── app/                      # Application package
│   ├── __init__.py           # Package initializer
│   ├── database.py           # Database connection and session management
│   ├── static/               # Static assets (CSS, JavaScript, images)
│   │   ├── css/              # CSS files
│   │   ├── js/               # JavaScript files
│   │   └── img/              # Image files
│   │
│   ├── api/                  # API routes
│   │   ├── __init__.py       # Package initializer
│   │   └── quiz_routes.py    # Quiz API routes
│   │
│   ├── models/               # Data models
│   │   ├── __init__.py       # Package initializer
│   │   ├── database.py       # SQLAlchemy database models
│   │   └── quiz.py           # Pydantic models for API
│   │
│   └── services/             # Business logic
│       ├── __init__.py       # Package initializer
│       └── quiz_service.py   # Quiz service functions
│
├── migrations/               # Alembic migrations
│   ├── env.py                # Alembic environment configuration
│   ├── script.py.mako        # Migration template
│   └── versions/             # Migration scripts
│       └── 001_initial.py    # Initial migration
│
└── templates/                # Jinja2 HTML templates
    ├── base.html             # Base template with common elements
    ├── index.html            # Home page template
    ├── quiz.html             # Quiz page template
    ├── quiz_details.html     # Quiz details page template
    └── records.html          # Records page template
```

## 🎮 How to Play

1. **Start the application**
   ```bash
   uvicorn main:app --reload
   ```

2. **Open your browser** and navigate to `http://localhost:8000`

3. **Create an account** or log in if you already have one

4. **Select the number of questions** (1-20)

5. **Choose a category** from the available options

6. **Answer each question** by selecting your choice

7. **View your results** and see how you performed

8. **Check your history** to track your progress over time

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

## 🗄️ Database Schema

The application uses a PostgreSQL database with the following main tables:

- **Users**: Stores user information including username, email, and password hash
- **Quizzes**: Stores quiz session information including category, difficulty, and date
- **Questions**: Stores individual questions with their correct answers and options
- **UserAnswers**: Stores user responses to questions for tracking performance
- **UserStats**: Aggregates user statistics like total quizzes taken, average score, etc.

## 🛠️ API Endpoints

| Endpoint                  | Method | Description                                   |
|---------------------------|--------|-----------------------------------------------|
| `/api/quiz`               | GET    | Get a list of available quizzes               |
| `/api/quiz/new`           | POST   | Create a new quiz session                     |
| `/api/quiz/{quiz_id}`     | GET    | Get details about a specific quiz             |
| `/api/quiz/{quiz_id}/submit` | POST | Submit answers for a quiz                     |
| `/api/user/stats`         | GET    | Get user statistics                           |
| `/api/user/history`       | GET    | Get user quiz history                         |

## 🔧 Environment Variables

Create a `.env` file in the root directory with the following variables:

```
# Database Connection
DATABASE_URL=postgresql://username:password@localhost/quiz_db

# API Settings
TRIVIA_API_URL=https://opentdb.com/api.php

# Application Settings
SECRET_KEY=your_secret_key_here
DEBUG=True
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/engrmumtazali0112/Robust-Multiple-Choice-Quiz-Game/issues).

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Development Roadmap

- [x] Basic quiz functionality
- [x] API integration with Open Trivia DB
- [x] Database integration with SQLAlchemy
- [x] User authentication system
- [ ] Leaderboards and social features
- [ ] Mobile responsive design
- [ ] User profile customization
- [ ] Custom quiz creation
- [ ] Multiplayer mode

## 🙏 Acknowledgements

A big thanks to [@EcodeCamp](https://github.com/EcodeCamp) for inspiring this project and encouraging developers to enhance their skills through practical coding challenges.

Special thanks to the Open Trivia Database for providing the free API that powers this application's questions.

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