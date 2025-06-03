import datetime
step_goal = int(input("\n What is your daily step goal"))
num_step = int(input("\n How many steps have you taken today"))

if num_step >= step_goal:
    print(
        f"🎉 You have completed your daily step target with a total {num_step} steps on {datetime.date.today()}")
elif num_step < step_goal:
    print(
        f"☹ you need an average of {step_goal - num_step} to complete your daily target")
elif num_step > step_goal:
    print(
        f"You have a congratulations you've exceeded your goal by {num_step - step_goal} steps")
