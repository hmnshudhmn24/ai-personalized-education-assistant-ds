import json
import random
import time

# Learning material for different styles
LESSON_BANK = {
    "visual": {
        "math": "Fractions visualized using pie charts and graphs.",
        "science": "Water cycle animated diagrams.",
        "history": "Timeline of World War II with historical photos."
    },
    "auditory": {
        "math": "Listen to step-by-step equation solving.",
        "science": "Audio clip on Newton’s laws.",
        "history": "Podcast on Civil Rights Movement."
    },
    "kinesthetic": {
        "math": "Cut paper to learn geometry hands-on.",
        "science": "Try a home experiment with baking soda and vinegar.",
        "history": "Build a diorama of an ancient city."
    }
}

# Quizzes for each subject
QUIZ_BANK = {
    "math": [
        {"q": "What is 5 + 3?", "a": "8"},
        {"q": "Solve: 12 - 7", "a": "5"},
        {"q": "What is 3 x 4?", "a": "12"}
    ],
    "science": [
        {"q": "What planet is known as the Red Planet?", "a": "mars"},
        {"q": "What gas do plants need for photosynthesis?", "a": "carbon dioxide"},
        {"q": "How many legs does an insect have?", "a": "6"}
    ],
    "history": [
        {"q": "Who was the first president of the USA?", "a": "george washington"},
        {"q": "In which year did World War II end?", "a": "1945"},
        {"q": "Who discovered America?", "a": "christopher columbus"}
    ]
}

# Survey to detect learning style
def detect_learning_style():
    print("Let's find your learning style.")
    questions = [
        ("I remember things better when I see pictures or charts.", "visual"),
        ("I prefer listening to explanations.", "auditory"),
        ("I like doing activities to learn.", "kinesthetic")
    ]
    score = {"visual": 0, "auditory": 0, "kinesthetic": 0}

    for question, style in questions:
        print(question)
        answer = input("Agree? (yes/no): ").strip().lower()
        if answer == "yes":
            score[style] += 1

    learning_style = max(score, key=score.get)
    print(f"\nDetected Learning Style: {learning_style.capitalize()}")
    return learning_style

# Generate lessons
def get_lessons(style):
    print("\nYour Personalized Lessons:")
    lessons = {}
    for subject in ["math", "science", "history"]:
        lesson = LESSON_BANK[style][subject]
        print(f"{subject.capitalize()}: {lesson}")
        lessons[subject] = lesson
        time.sleep(1)
    return lessons

# Quiz function
def start_quiz():
    print("\nLet's take a short quiz!")
    total = 0
    correct = 0
    for subject, questions in QUIZ_BANK.items():
        q = random.choice(questions)
        ans = input(f"{subject.capitalize()} - {q['q']}: ").strip().lower()
        if ans == q["a"]:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! Correct answer: {q['a']}")
        total += 1
    print(f"\nQuiz Complete! Score: {correct}/{total}")

# Save progress
def save_progress(username, style, lessons):
    data = {
        "user": username,
        "learning_style": style,
        "lessons": lessons
    }
    filename = f"{username}_progress.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Progress saved to {filename}")

# Main chatbot function
def education_assistant():
    print("=== AI-Powered Personalized Education Assistant ===")
    name = input("Enter your name: ").strip()
    style = detect_learning_style()
    lessons = get_lessons(style)
    start_quiz()
    save_progress(name, style, lessons)
    print("\nThanks for learning with us!")

if __name__ == "__main__":
    education_assistant()
