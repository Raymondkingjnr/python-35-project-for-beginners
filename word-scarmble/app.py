import random

# Because the code will be rununing indefinitely, we need to use a while loop
while True:
    word = input("\nEnter a word to scramble (or 'quit'): ")
    if word.lower() == "quit":
        print("👋 Goodbye")
        break

    letters = list(word)
    random.shuffle(letters)
    print("Scrambled word:", "".join(letters))
