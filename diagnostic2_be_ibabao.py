def calculate_total(topping_count):
    return 10.00 + (topping_count * 1.50)

topping_count = 0

print("Welcome to Zean's Pizza Place!")

while True:
    topping = input("Enter a topping(pepperoni, mushrooms, extra cheese) or 'done' to finish: ").lower()
    if topping == 'done':
        break
    elif topping in ['pepperoni', 'mushrooms', 'extra cheese']:
        topping_count += 1
    else:
        print("Invalid topping. Please choose from pepperoni, mushrooms, or extra cheese.")

total = calculate_total(topping_count)

discount_code = input("Enter discount code (if any): ")
if discount_code == "PYTHON20":
    total = total * 0.8
    print(f"Discount applied! Your new total is: ${total:.2f}")
    print(f"You just saved ${total * 0.2:.2f} with the discount code!")
else:
    print("No discount applied.")

print(f"Your final total is: ${total:.2f}")
print("Thank you for dining with us!")
