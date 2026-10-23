
import random


# ASCII gallows stages: one stage for each number of wrong guesses
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]

# Words used in the game
WORD_LIST = [
    "python", "computer", "program", "developer",
    "keyboard", "science", "machine", "learning",
    "student", "internet", "software", "algorithm",
    "network", "project", "digital"
]

MAX_ATTEMPTS = 6


def choose_word():
    """Choose a random word from the word list."""
    return random.choice(WORD_LIST).lower()


def display_word(secret_word, guessed_letters):
    """Show guessed letters and hide the remaining letters."""
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def display_game(secret_word, guessed_letters, wrong_guesses):
    """Display the gallows, masked word, and guessed letters."""
    print(HANGMAN_STAGES[wrong_guesses])
    print("Word:", display_word(secret_word, guessed_letters))

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    print(f"Incorrect guesses: {wrong_guesses}/{MAX_ATTEMPTS}")


def play_game():
    """Run one complete round of Hangman."""
    secret_word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("\n" + "=" * 35)
    print("       HANGMAN WORD GAME")
    print("=" * 35)
    print("Guess the hidden word one letter at a time.")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed.")

    while wrong_guesses < MAX_ATTEMPTS:
        display_game(secret_word, guessed_letters, wrong_guesses)

        if all(letter in guessed_letters for letter in secret_word):
            break

        guess = input("\nEnter a letter: ").strip().lower()

        # Validate the user's input
        if len(guess) != 1 or not guess.isalpha() or not guess.isascii():
            print("Invalid input. Enter one English letter (A-Z).")
            continue

        # Prevent duplicate guesses from costing an attempt
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Correct! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word.")

    # Show the final result
    display_game(secret_word, guessed_letters, wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
    else:
        print("\nGame over! You ran out of attempts.")
        print("The correct word was:", secret_word)


def main():
    """Allow the user to play multiple rounds."""
    while True:
        play_game()

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
