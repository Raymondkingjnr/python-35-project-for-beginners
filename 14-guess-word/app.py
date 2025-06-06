import random

words = ["python", "java", "javascript", "ruby", "swift", "kotlin"]

while True:
    chooseword = random.choice(words)
    scrambled_word = list(chooseword)
    random.shuffle(scrambled_word)
    print("\nGuess the word:",  "".join(scrambled_word))

    guess = input("Your guess (or 'quit' to exit): ")
    if guess.lower() == "quit":
        print("👋 Goodbye")
        break
    if guess.lower() == chooseword:
        print("🎉 Correct! The word was:", chooseword)
    else:
        print("❌ Incorrect! Try again.")
        print("The correct word was:", chooseword)
