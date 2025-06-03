import random
# import math
import datetime
import os
import sys
import time

random_number = random.randint(1, 10)
print(f"Randon number is {random_number}")

print("")
# choose a random elemement from a list
fruit = ["mango", "apple", "cheery"]
random_fruit = random.choice(fruit)
print(f"Randon fruit is {random_fruit}")


# Shuffle
print(" ")
random.shuffle(fruit)
print(f"shuffled list {fruit}")

print("")
current_time = datetime.datetime.now()
print(f"current date and time {current_time}")
print(f"Today's date: {datetime.date.today()}")
print(f"Current year: {datetime.date.today().year}")

print("")

print(f"Platform: {sys.platform}")
