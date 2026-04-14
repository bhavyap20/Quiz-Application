class QuizApp:
    def __init__(self):
        self.questions = [
            {
                "question": "What does CPU stand for?",
                "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Unit"],
                "answer": "B"
            },
            {
                "question": "Which language is used for AI?",
                "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
                "answer": "A"
            },
            {
                "question": "What is OOPS?",
                "options": ["A. Programming Paradigm", "B. Operating System", "C. Database", "D. Network"],
                "answer": "A"
            },
            {
                "question": "Which protocol is connection-oriented?",
                "options": ["A. UDP", "B. TCP", "C. IP", "D. HTTP"],
                "answer": "B"
            },
            {
                "question": "Which data structure uses FIFO?",
                "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
                "answer": "B"
            }
        ]
        self.score = 0

    def start_quiz(self):
        print("\n🎯 Welcome to the Quiz Application\n")

        for i, q in enumerate(self.questions):
            print(f"\nQ{i+1}: {q['question']}")
            for option in q["options"]:
                print(option)

            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer == q["answer"]:
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer is {q['answer']}")

        self.show_result()

    def show_result(self):
        print("\n📊 Quiz Completed!")
        print(f"Your Score: {self.score}/{len(self.questions)}")

        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 80:
            print("🔥 Excellent!")
        elif percentage >= 50:
            print("👍 Good Job!")
        else:
            print("📘 Keep Practicing!")


# Run the quiz
if __name__ == "__main__":
    quiz = QuizApp()
    quiz.start_quiz()