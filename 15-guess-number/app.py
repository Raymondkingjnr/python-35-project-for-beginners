import random

print("🎮 Welcome to the Number Guessing Game! 🎮")
print("🤔 I'm thinking of a number between 1 and 100. You have 10 attempts. 🔢")

playing = True
while playing:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    game_over = False

    while attempts < max_attempts and not game_over:
        try:
            guess = int(
                input(f"Attempt {attempts + 1}/{max_attempts}: What's your guess? "))

        except ValueError:
            print("🚫 Please enter a valid number! 🚫")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low! try a higher number 💹")
        elif guess > secret_number:
            print("📈 Too high! try a lower number 📉")
        else:
            print(
                f"🎉 Congratulations! You've guessed the number {secret_number} in {attempts} attempts! 🎉")
            game_over = True
        if attempts < max_attempts and not game_over:
            print(
                f"You have {max_attempts - attempts} attempts left. Good Luck! 🍀")
    if not game_over:
        print("Game Over! The secret number was:", secret_number)

    play_again = input(
        "Do you want to play again? (yes/no): ").strip().lower()
    if play_again.startswith("n"):

        print("Thanks for playing! Goodbye! 👋")
        playing = False
