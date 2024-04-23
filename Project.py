print("Welcome to the tip calculator!")
totalBill = input("What was the total bill? $")
tipPercentage = input("How much tip would you like to give? 10, 12, or 15? ")
numberOfPeople = input("How many people to split the bill? ")

result = float(totalBill) * (1 + int(tipPercentage) / 100) / \
    int(numberOfPeople)

print(f"Each person should pay: ${round(result, 2)}")
