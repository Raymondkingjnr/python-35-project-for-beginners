vowel = ["a", "e", "i", "u"]

while True:
    text = input("\nenter some text (or quit): ")

    if text.lower() == "quite":
        print(f"👋 goodbye")
        break

    vowel_count = 0

    for letter in text.lower():
        if letter in vowel:
            vowel_count += 1

    print(f"this text has {vowel_count} vowels")
