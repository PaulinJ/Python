import random

print("🎲 --- Guessing Game with Python --- 🎲")
print("   -------------------------------    ")

secret_number = random.randint(1, 10)

print("🤔 I'm thinking of a number between 1 and 10. Can you guess it?")

# Get valid guess
while True:
    try:
        guess = int(input("🔢 Enter your guess: "))
        break
    except ValueError:
        print("❌ Invalid input! Please enter a number between 1 and 10.")

while guess != secret_number:
    while True:
        try:
            guess = int(input("❌ Wrong! Lol. Try again: "))
            break
        except ValueError:
            print("❌ That's not a number! Try again:")

answer = input("✅ Correct! 🎉 Want to continue? Enter yes or no: ").lower()

while answer not in ["yes", "no"]:
    answer = input("❓ Please enter 'yes' or 'no': ").lower()

while answer == "yes":
    secret_number = random.randint(1, 10)
    print("\n🔁 New round!")
    print("🤔 I'm thinking of a number between 1 and 10. Guess again!")

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

    while guess != secret_number:
        while True:
            try:
                guess = int(input("❌ Nope! Try again: "))
                break
            except ValueError:
                print("❌ That's not a number! Try again:")

    answer = input("✅ Nailed it! Want to play again? Enter yes or no: ").lower()
    while answer not in ["yes", "no"]:
        answer = input("❓ Please enter 'yes' or 'no': ").lower()

print("🎮 Thanks for playing! Bye 👋😄")
