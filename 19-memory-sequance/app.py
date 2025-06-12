import random
import os
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


print("\n=== 🧠 MEMORY SEQUENCE GAME 🧠 ===")
print("✨ Remember the sequence and type it back! ✨")
print("\nRules:")
print("- Watch as numbers appear one by one")
print("- After the sequence is shown, type it back in order")
print("- Each round adds one more number to remember")
print("- How far can you go? 🏆\n")

input("Press Enter to start...")

sequance = []
current_round = 1
game_over = False

while not game_over:
    sequance.append(random.randint(1, 9))

    clear_screen()
    print(f"\n===Round {current_round} ===")
    print(f"Remeber this sequance of {len(sequance)} numbers: ")

    for number in sequance:
        time.sleep(0.7)
        print(f"\n{number}")
        time.sleep(0.7)
        clear_screen()

    print(f"\nNow repate the sequance by tying each number, seperated by space: ")
    player_answer = input("> ")

    try:
        player_sequance = [int(num) for num in player_answer.split()]
    except ValueError:
        print("❌Please enter numbers only")
        game_over = True
        continue

    if player_sequance == sequance:
        print(f"🙌 you remeber all {len(sequance)} numbers")
        current_round += 1
        time.sleep(2)
    else:
        print(f"Game Over Your rememberd all {current_round - 1} numbers!")
        print(
            f"The correct sequance was: {"".join(str(num) for num in sequance)}")
        game_over = True

    if game_over:
        play_again = input("\nDo you want to play (yes/no): ").lower()

        if play_again.startswith("y"):
            continue
        else:
            print("Good Bye")
            break
