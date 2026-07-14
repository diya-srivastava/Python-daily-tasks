import json
import os

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which planet is called the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. bool", "C. str", "D. float"],
        "answer": "B"
    }
]

file_name = "highscore.json"


def get_high_score():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return {"name": "", "score": 0}


def save_high_score(name, score):
    with open(file_name, "w") as file:
        json.dump({"name": name, "score": score}, file)


while True:
    print("\n====== QUIZ GAME ======")
    print("1. Play Quiz")
    print("2. High Score")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        player = input("Enter your name: ")
        score = 0

        for q in questions:
            print("\n" + q["question"])

            for option in q["options"]:
                print(option)

            ans = input("Your answer: ").upper()

            if ans == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")

        print(f"\nYour final score is {score}/{len(questions)}")

        high = get_high_score()

        if score > high["score"]:
            print("New High Score!")
            save_high_score(player, score)

    elif choice == "2":
        high = get_high_score()
        print("\nHigh Score")
        print("Player:", high["name"])
        print("Score :", high["score"])

    elif choice == "3":
        print("Thanks for playing!")
        break

    else:
        print("Please enter a valid option.")