import time

while True:
    try:
        sec = int(input("\nEnter seconds to count down from: "))

        if sec <= 0:
            print("❌ please enter a positive value")
        print(f"Starting count down from {sec} seconds")

        for i in range(sec, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("COUNTDOWN COMPLETE")
        again = input("\n Start another countdown? (yes/no): ").lower().strip()
        if not again.startswith("y"):
            print("👋 Goodbye")
            break
    except ValueError:
        print("Please enter a positive number")
