# INTRODUCTION
# Create a program using maths and f-Strings that tells us how many
# weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time
# left if this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age
# has left until age 90.
# Warning your output should match the Example Output format exactly, even the positions
# of the commas and ull stops.
# Example Input: 56
# Example Output: You have 1768 weeks left.

maxAge = 90
weeksPerYear = 52
age = input("Give me your age: ")
remainingYears = 90 - int(age)
remainingWeeks = remainingYears * weeksPerYear
print(f"You have {remainingWeeks} weeks left.")
