import random
coin = ["heads", "tails"]

while True:
    choice = input("\nEnter your guess (heads or tails): ")
    if choice != "heads" and choice != "tails":
        print("📛 please enter 'heads' or 'tail' ")
        continue
    ai_choice = random.choice(coin)
    if choice.lower() == ai_choice:
        print(f"The coin shows {ai_choice}")
        print("You guessed correctly! you win")
    elif choice.lower() != ai_choice:
        print(f"The coin shows {ai_choice}")
        print("Sorry wrong guess. Trry again")
    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() == "no":
        break
