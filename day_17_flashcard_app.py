
import random

flashcards = [
    {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def"
    },
    {
        "question": "What is the result of 5 ** 2?",
        "answer": "25"
    },
    {
        "question": "Which data type stores True or False?",
        "answer": "bool"
    },
    {
        "question": "Which keyword is used to create a loop over a sequence?",
        "answer": "for"
    }
]


def study_flashcards():
    cards = flashcards.copy()
    random.shuffle(cards)

    score = 0
    incorrect_cards = []

    print("\n===== FLASHCARD STUDY APP =====")
    print(f"You have {len(cards)} flashcards.")
    print("Type 'quit' to end the session.\n")

    for card in cards:
        print("Question:", card["question"])

        choice = input(
            "Press Enter to reveal the answer, or type 'quit': "
        ).strip().lower()

        if choice == "quit":
            break

        print("Answer:", card["answer"])

        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == card["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print("Not quite!\n")
            incorrect_cards.append(card)

    attempted = score + len(incorrect_cards)

    print("\n===== SESSION SUMMARY =====")
    print("Correct answers:", score)
    print("Incorrect answers:", len(incorrect_cards))
    print("Questions attempted:", attempted)

    if attempted > 0:
        accuracy = (score / attempted) * 100
        print(f"Accuracy: {accuracy:.1f}%")

    if incorrect_cards:
        print("\n===== REVIEW YOUR MISTAKES =====")

        for card in incorrect_cards:
            print("Question:", card["question"])
            print("Correct answer:", card["answer"])
            print()

    else:
        print("\nGreat job! No incorrect answers.")


while True:
    print("\n1. Start studying")
    print("2. Exit")

    option = input("Choose an option: ").strip()

    if option == "1":
        study_flashcards()
    elif option == "2":
        print("Goodbye! Keep learning.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
