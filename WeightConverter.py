print("⚖️ --- Weight Converter --- ⚖️")
print("   -------------------------------    ")

answer = "yes"

while answer.lower() != "no":
    # Get weight with error checking
    while True:
        try:
            weight = float(input('⚖️  Enter weight: '))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


    unit = input('(L)bs or (K)g: ').upper()
    while unit not in ['L', 'K']:
        print("❌ Invalid unit. Please enter 'L' for pounds or 'K' for kilograms.")
        unit = input('(L)bs or (K)g: ').upper()

    # Conversion
    if unit == "L":
        converted = weight * 0.45
        print(f"📏 You weigh {converted:.2f} kilograms.")
    else:
        converted = weight / 0.45
        print(f"📏 You weigh {converted:.2f} pounds.")


    answer = input("🔁 Do you want to continue? (yes/no): ").lower()
    while answer not in ['yes', 'no']:
        answer = input("❓ Please enter 'yes' or 'no': ").lower()

print("👋 Thanks for using the converter!")
