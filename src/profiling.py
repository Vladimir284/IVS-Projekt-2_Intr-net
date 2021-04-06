import math_lib

# Read and split
input_string = input()
array_of_numbers = input_string.split(" ")

# Declare all used varriable
amount_of_numbers = len(array_of_numbers)
sum_of_numbers = 0.0
average_of_numbers = 0.0
sum_of_squared_difference = 0.0
standard_deviation = 0.0
difference_of_element = 0.0
square_of_difference_of_element = 0.0
variance = 0.0

# Summary of all the elements enetered
for number_string in array_of_numbers:
    if number_string.isdigit():
        sum_of_numbers = math_lib.summary(float(number_string), sum_of_numbers)

# Average of elements
average_of_numbers = math_lib.division(sum_of_numbers, amount_of_numbers)

# Summary of difference of each element with average
for number_string in array_of_numbers:
    if number_string.isdigit():
        difference_of_element = math_lib.subtraction(float(number_string), average_of_numbers)
        square_of_difference_of_element = math_lib.nth_power(difference_of_element, 2)
        sum_of_squared_difference = math_lib.summary(sum_of_squared_difference, square_of_difference_of_element)

# Last counting, I promise:)
variance = math_lib.division(sum_of_squared_difference, amount_of_numbers)
standard_deviation = math_lib.nth_root(2, variance)

print(standard_deviation)