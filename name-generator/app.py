import random
first = ["joe", "star", "moon", "sun", "mars"]
last = ["trigger", "muna", "gallager", "chuks"]

count = int(input("How many names do you want: "))

for _ in range(count):
    first_name = random.choice(first).capitalize()
    last_name = random.choice(last)
    print(f"{first_name}{last_name}")

print("")
print("Now generate userName")
firstName = input("Enter Your First Name: ")
lastName = input("Enter Your Last Name: ")
fullName = firstName + lastName

userName = list(fullName)
random.shuffle(userName)
print("username:", "".join(userName))
