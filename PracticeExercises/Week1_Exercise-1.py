#Exercise to print the number is even or odd
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
user_input = int(input("Enter a number: "))

# Check if the number is odd or even
result = check_odd_even(user_input)

# Display the result
print(f"The number {user_input} is {result}.")
