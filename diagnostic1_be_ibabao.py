def calculate_space_weight(earth_weight, destination):
    if destination == "moon":
        return earth_weight * 0.165
    elif destination == "mars":
        return earth_weight * 0.38
    elif destination == "jupiter":
        return earth_weight * 2.34
    else:
        return "Invalid destination. Please choose Moon, Mars, or Jupiter."
        return 0

earth_weight = float(input("Enter your weight on Earth (in kg): "))
destination = input("Enter your destination (Moon, Mars, or Jupiter): ").lower()

new_weight = calculate_space_weight(earth_weight, destination)

print(f"Your weight on {destination.capitalize()} would be: {new_weight:.2f} kg")


    