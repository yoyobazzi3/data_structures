# Allows the user to input numbers separated by spaces
numbers_input = input("Enter numbers separated by spaces: ")

# This line converts the strings into float numbers
numbers = [float(n) for n in numbers_input.split()]

# Will not repeat numbers in the array
unique_numbers = list(set(numbers))

# Sorts the numbers in descending order
unique_numbers.sort(reverse=True)

# Checks if there are at least two unique numbers
if len(unique_numbers) < 2:
    print("Need at least two unique numbers to find the second largest.")
else:
    # Get the second largest number
    second_largest = unique_numbers[1]
    print("The second largest number is:", second_largest)
