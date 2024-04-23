# 1st input: enter height in meters e.g.: 1.65
height = input("Enter height in meters: ")
# 2nd input: enter weight in kilograms e.g.: 72
weight = input("Enter weight in kilograms: ")
# Don't change the code above

# Write your code below this line
bmi = float(weight) / float(height) ** 2.0
print(f"Body Mass Index (BMI) is {round(bmi, 2)}")
