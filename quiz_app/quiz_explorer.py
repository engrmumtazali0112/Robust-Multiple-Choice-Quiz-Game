import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
from tabulate import tabulate

# Quiz categories from your code
CATEGORIES = {
    "General Knowledge": 9,
    "Books": 10,
    "Film": 11,
    "Music": 12,
    "Television": 14,
    "Video Games": 15,
    "Board Games": 16,
    "Science & Nature": 17,
    "Computers": 18,
    "Mathematics": 19,
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27,
    "Vehicles": 28,
    "Comics": 29,
    "Anime & Manga": 31,
    "Cartoons & Animation": 32
}

# Create an inverted dictionary for easy lookup (id -> name)
CATEGORIES_BY_ID = {id: name for name, id in CATEGORIES.items()}

def connect_to_db():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        # Connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host="localhost",
            database="quiz_db",
            user="postgres",
            password="password"  # Replace with your actual password
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        if conn is not None:
            conn.close()
        return None

def get_all_quizzes(conn):
    """Get all quizzes from the database"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT id, category, num_questions, current_score, created_at, user_id
        FROM quizzes
        ORDER BY created_at DESC
    """)
    quizzes = cursor.fetchall()
    cursor.close()
    
    # Convert category IDs to names
    for quiz in quizzes:
        quiz['category_name'] = CATEGORIES_BY_ID.get(quiz['category'], 'Unknown')
    
    return quizzes

def get_quiz_details(conn, quiz_id):
    """Get detailed information about a specific quiz"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    
    # Get quiz header information
    cursor.execute("""
        SELECT id, category, num_questions, current_score, created_at, user_id
        FROM quizzes
        WHERE id = %s
    """, (quiz_id,))
    quiz = cursor.fetchone()
    
    if not quiz:
        cursor.close()
        return None
    
    # Add category name
    quiz['category_name'] = CATEGORIES_BY_ID.get(quiz['category'], 'Unknown')
    
    # Get questions for this quiz
    cursor.execute("""
        SELECT id, question, correct_answer
        FROM questions
        WHERE quiz_id = %s
    """, (quiz_id,))
    questions = cursor.fetchall()
    quiz['questions'] = []
    
    # For each question, get options
    for question in questions:
        cursor.execute("""
            SELECT id, text
            FROM question_options
            WHERE question_id = %s
        """, (question['id'],))
        options = cursor.fetchall()
        question['options'] = options
        quiz['questions'].append(question)
    
    # Get quiz result if available
    cursor.execute("""
        SELECT id, score, total_questions, percentage, feedback, created_at
        FROM quiz_results
        WHERE quiz_id = %s
    """, (quiz_id,))
    result = cursor.fetchone()
    quiz['result'] = result
    
    cursor.close()
    return quiz

def get_quiz_results(conn):
    """Get all quiz results"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT 
            qr.id AS result_id,
            qr.quiz_id,
            qr.score,
            qr.total_questions,
            qr.percentage,
            qr.feedback,
            qr.created_at,
            q.category
        FROM quiz_results qr
        JOIN quizzes q ON qr.quiz_id = q.id
        ORDER BY qr.created_at DESC
    """)
    results = cursor.fetchall()
    cursor.close()
    
    # Convert category IDs to names
    for result in results:
        result['category_name'] = CATEGORIES_BY_ID.get(result['category'], 'Unknown')
    
    return results

def display_quizzes(quizzes):
    """Display quizzes in a formatted table"""
    if not quizzes:
        print("No quizzes found.")
        return
    
    # Convert to pandas DataFrame for better display
    df = pd.DataFrame(quizzes)
    
    # Select and rename columns
    display_df = df[['id', 'category_name', 'num_questions', 'current_score', 'created_at']]
    display_df = display_df.rename(columns={
        'id': 'Quiz ID',
        'category_name': 'Category',
        'num_questions': 'Questions',
        'current_score': 'Score',
        'created_at': 'Created'
    })
    
    print("\n=== QUIZZES ===")
    print(tabulate(display_df, headers='keys', tablefmt='pretty', showindex=False))

def display_quiz_details(quiz):
    """Display detailed information about a quiz"""
    if not quiz:
        print("Quiz not found.")
        return
    
    print(f"\n=== QUIZ DETAILS ===")
    print(f"ID: {quiz['id']}")
    print(f"Category: {quiz['category_name']}")
    print(f"Number of Questions: {quiz['num_questions']}")
    print(f"Current Score: {quiz['current_score']}")
    print(f"Created: {quiz['created_at']}")
    
    print("\n--- Questions ---")
    for i, question in enumerate(quiz['questions'], 1):
        print(f"\n{i}. {question['question']}")
        print(f"   Correct Answer: {question['correct_answer']}")
        print("   Options:")
        for j, option in enumerate(question['options'], 1):
            print(f"     {j}. {option['text']}")
    
    if quiz['result']:
        print("\n--- Quiz Result ---")
        print(f"Score: {quiz['result']['score']}/{quiz['result']['total_questions']}")
        print(f"Percentage: {quiz['result']['percentage']}%")
        print(f"Feedback: {quiz['result']['feedback']}")
        print(f"Completed: {quiz['result']['created_at']}")

def display_quiz_results(results):
    """Display quiz results in a formatted table"""
    if not results:
        print("No quiz results found.")
        return
    
    # Convert to pandas DataFrame for better display
    df = pd.DataFrame(results)
    
    # Select and rename columns
    display_df = df[['quiz_id', 'category_name', 'score', 'total_questions', 'percentage', 'created_at']]
    display_df = display_df.rename(columns={
        'quiz_id': 'Quiz ID',
        'category_name': 'Category',
        'score': 'Score',
        'total_questions': 'Total',
        'percentage': 'Percentage',
        'created_at': 'Created'
    })
    
    print("\n=== QUIZ RESULTS ===")
    print(tabulate(display_df, headers='keys', tablefmt='pretty', showindex=False))

def get_quiz_statistics(conn):
    """Get quiz statistics by category"""
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""
        SELECT 
            q.category,
            COUNT(qr.id) AS total_quizzes,
            AVG(qr.percentage) AS average_score
        FROM quiz_results qr
        JOIN quizzes q ON qr.quiz_id = q.id
        GROUP BY q.category
        ORDER BY average_score DESC
    """)
    stats = cursor.fetchall()
    cursor.close()
    
    # Convert category IDs to names
    for stat in stats:
        stat['category_name'] = CATEGORIES_BY_ID.get(stat['category'], 'Unknown')
        stat['average_score'] = round(stat['average_score'], 2)
    
    return stats

def display_quiz_statistics(stats):
    """Display quiz statistics in a formatted table"""
    if not stats:
        print("No quiz statistics available.")
        return
    
    # Convert to pandas DataFrame for better display
    df = pd.DataFrame(stats)
    
    # Select and rename columns
    display_df = df[['category_name', 'total_quizzes', 'average_score']]
    display_df = display_df.rename(columns={
        'category_name': 'Category',
        'total_quizzes': 'Quizzes',
        'average_score': 'Avg Score %'
    })
    
    print("\n=== QUIZ STATISTICS ===")
    print(tabulate(display_df, headers='keys', tablefmt='pretty', showindex=False))

def main():
    """Main function to explore the quiz database"""
    conn = connect_to_db()
    if not conn:
        return
    
    try:
        print("\nWelcome to the Quiz Database Explorer!")
        print("=====================================")
        
        while True:
            print("\nChoose an option:")
            print("1. List all quizzes")
            print("2. View quiz details (requires quiz ID)")
            print("3. List quiz results")
            print("4. View quiz statistics")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                quizzes = get_all_quizzes(conn)
                display_quizzes(quizzes)
            
            elif choice == '2':
                quiz_id = input("Enter the quiz ID: ")
                quiz = get_quiz_details(conn, quiz_id)
                display_quiz_details(quiz)
            
            elif choice == '3':
                results = get_quiz_results(conn)
                display_quiz_results(results)
            
            elif choice == '4':
                stats = get_quiz_statistics(conn)
                display_quiz_statistics(stats)
            
            elif choice == '5':
                print("\nThank you for using the Quiz Database Explorer!")
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()