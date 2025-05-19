<div align="center">

# 🎮 Robust Multiple Choice Quiz Game 🎮

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.28+-brightgreen?style=for-the-badge&logo=python&logoColor=white)
![Open Trivia DB](https://img.shields.io/badge/Open_Trivia_DB-API-orange?style=for-the-badge)
![Error Handling](https://img.shields.io/badge/Error_Handling-Robust-red?style=for-the-badge)

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmZrcmFvc2JvODlwaHRmYm9mZnJ5aXNlbGc2MHkyN2o1NDI3N3M0ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCScwdMAohPCq76/giphy.gif" width="400" alt="Quiz Animation">
</p>

A robust command-line quiz game designed to test your knowledge with multiple-choice questions from various categories.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

</div>

## 📋 Description
https://github.com/engrmumtazali0112/Robust-Multiple-Choice-Quiz-Game.git
This interactive quiz game fetches random questions using the Open Trivia Database API and provides a fallback to local questions if the API is unavailable. Challenge yourself with questions from more than 20 different categories!

## ✨ Key Features

- 🐍 **Python-Powered**: Clean, efficient core logic and game functionality
- 🌐 **API Integration**: Dynamically fetches quiz questions from Open Trivia Database
- 🔄 **Randomization**: Ensures the order of answers is randomized for each question
- ⚠️ **Error Handling**: Seamlessly provides local questions if the API is unavailable
- 🎯 **Multiple Categories**: Choose from 22+ different quiz categories
- 👤 **User-Friendly Design**: Simple and intuitive multiple-choice format
- 📈 **Performance Feedback**: Receive personalized feedback based on your score
## 🎥 Demo
### Quiz Game Features

<details>
<summary>Click to view Demo</summary>

| ![Quiz Question Screen](https://github.com/user-attachments/assets/8f2ad6f3-77b2-4ece-acd2-43564b9b2fdd) | ![Answer Selection](https://github.com/user-attachments/assets/5cbb0fc4-8e4e-496a-a0cf-0fd4be3e751c) | ![Score Summary](https://github.com/user-attachments/assets/2439b7c5-13bb-49e9-ad0b-1a2245e37e34) | 
| --- | --- | --- |
| **Quiz Question Screen**: Interactive multiple-choice question interface where questions are displayed and randomized answer options are provided. | **Answer Selection**: Users select an answer from the options provided in the quiz interface. | **Score Summary**: Final score feedback based on the user's correct answers, including a percentage and performance summary. |

| ![Game Feedback](https://github.com/user-attachments/assets/c1e981ba-a33d-41d9-9ac3-13aa2ae6c4ee) | ![Gameplay Example](https://github.com/user-attachments/assets/2c5bee0f-9cda-41d0-a913-bf93e502a9f2) | ![User Result](https://github.com/user-attachments/assets/ba52b610-3711-451b-a2fd-3abc46e46780) |
| --- | --- | --- |
| **Game Feedback**: Visual feedback provided after each question or at the end of the game, summarizing the user's performance. | **Gameplay Example**: An example of the user’s progress during the quiz, showing how the system updates after each response. | **User Result**: The results page displaying the final score and detailed analysis based on the user's answers. |

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

3. **Install required dependencies**
   ```bash
   pip install requests
   ```

## 🎮 How to Play

1. **Run the game**
   ```bash
   python quiz_game.py
   ```

2. **Select the number of questions** (1-20)
3. **Choose a category** from the available options
4. **Answer each question** by entering the number of your choice (1-4)
5. **Receive feedback** on your performance

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

## 🧩 Project Structure

```
Robust-Multiple-Choice-Quiz-Game/
├── README.md
├── quiz_game.py
└── requirements.txt
```

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
