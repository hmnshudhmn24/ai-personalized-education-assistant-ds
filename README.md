# AI-Powered Personalized Education Assistant

An interactive Python-based education assistant that adapts to a student's learning style to deliver personalized lessons, interactive quizzes, and track progress. It uses simple AI techniques to recommend content that fits visual, auditory, or kinesthetic learning preferences.

## Features

- Detects a student's preferred learning style through a short survey
- Generates tailored lessons in Math, Science, and History
- Provides interactive quizzes with instant feedback
- Saves the user's progress in a JSON file
- Command-line interface for simple and accessible use

## How It Works

1. The user is asked a few questions to determine their learning style (Visual, Auditory, or Kinesthetic).
2. Based on the detected style, subject-specific lesson content is generated.
3. A short quiz is presented to assess basic knowledge.
4. The session progress is saved locally in a structured JSON file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/personalized-education-assistant.git
   cd personalized-education-assistant
   ```

2. Run the script:
   ```bash
   python education_assistant.py
   ```

> No external libraries are required.

## Example Output

```
=== AI-Powered Personalized Education Assistant ===
Enter your name: Alice
Let's find your learning style.
I remember things better when I see pictures or charts.
Agree? (yes/no): yes
...

Detected Learning Style: Visual

Your Personalized Lessons:
Math: Fractions visualized using pie charts and graphs.
Science: Water cycle animated diagrams.
History: Timeline of World War II with historical photos.

Let's take a short quiz!
Math - What is 5 + 3?: 8
Correct!
...

Quiz Complete! Score: 3/3
Progress saved to Alice_progress.json
Thanks for learning with us!
```

## Files

- `education_assistant.py` - Main source code
- `yourname_progress.json` - Automatically generated progress file

## License

This project is open-source and free to use under the MIT License.
