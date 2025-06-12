import random
import time

word_pairs = {
    "sky": ["blue", "cloud", "bird", "fly", "sun"],
    "water": ["drink", "ocean", "swim", "fish", "boat"],
    "food": ["eat", "cook", "tasty", "meal", "restaurant"],
    "music": ["song", "dance", "listen", "band", "rhythm"],
    "book": ["read", "story", "page", "author", "library"],
    "tree": ["leaf", "green", "forest", "wood", "shade"],
    "car": ["drive", "road", "wheel", "travel", "speed"],
    "dog": ["pet", "bark", "walk", "loyal", "puppy"]
}

print("\n=== WORD ASSOCIATION GAME ===")
print("Respond with a related word quickly")

score = 0
rounds = 0

while True:
    prompt = random.choice(list(word_pairs.keys()))
    related_words = word_pairs[prompt]

    print(f"\n Prompt word: {prompt.upper()}")
    print("Quick! Type a word related to this prompt!")

    start_time = time.time()

    responds = input("> ").lower().strip()
    response_time = time.time() - start_time

    print("reponse time", response_time)

    if responds in related_words:
        points = max(1, 5 - int(response_time))
        score += points
        print(
            f"Good word association, +{points} points (answered in {response_time:.1f}s)")
    else:
        print(
            f"Not a common association. Related words included: {','.join(related_words)}")
    round = + 1
    print(f"score: {score}/{round + 5} possible points")

    if input("\n Play again? (yes/no): ").lower().startswith("n"):
        print(f"Final score: {score}. Thanks for playing")
        break
