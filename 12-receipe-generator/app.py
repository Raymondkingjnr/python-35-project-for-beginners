import random

print("👩‍🍳 RANDOM RECIPE GENERATOR 👩‍🍳")

proteins = ["chicken", "beef", "tofu", "fish", "eggs"]
veggies = ["broccoli", "carrots", "spinach", "bell peppers", "mushrooms"]
carbs = ["rice", "pasta", "potatoes", "quinoa", "bread"]
methods = ["baked", "grilled", "stir-fried", "roasted", "sautéed"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]

while True:
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flavor = random.choice(flavors)

    print(
        f"\nYour random receipe: {flavor} {method} {protein} with {veggie} and {carb}")

    if input("\n generate another one? (y/n): ").lower().startswith("y"):
        print("👋 Goosbye")
        break
