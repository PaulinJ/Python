print("🚗 --- Welcome to the Python Car Game! --- 🚦")
print("Type 'help' to see what you can do.")

car_started = False

while True:
    command = input("💬 What do you want to do? ").lower()

    if command == "start":
        if car_started:
            print("🔁 The car is already started! You wanna flood the engine? 😅")
        else:
            car_started = True
            print("🚙 Vroom! The car has started. Let's ride!")

    elif command == "stop":
        if not car_started:
            print("🛑 Whoa there! The car is already stopped.")
        else:
            car_started = False
            print("💤 The car is now off. Taking a break, huh?")

    elif command == "help":
        print("""
🧭 Commands you can use:
 - start ➡️ Start the car
 - stop  ⛔ Stop the car
 - help  🆘 Show this help message
 - quit  👋 Exit the game
""")

    elif command == "quit":
        print("👋 Exiting game... Drive safe out there!")
        break

    else:
        print("❓ I don't understand that command. Type 'help' to see options.")
