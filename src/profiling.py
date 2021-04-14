## @package profiling
# @file profiling.py
# @brief Module for computing standard deviation
# @brief Inside varriables that store number are initilaized to zero
# @note \f$ s = \sqrt{\frac{1}{N-1} \cdot (\sum_{i=1}^{N} x_{i}^2-N \cdot \overline{x}^2})\f$
# @param numbers Sequence of numbers from stdin

import math_lib

# Read and split
##
# Input string with numbers separated by empty space
input_string = input()
##
# Separated numbers from #input_string stored in array
array_of_numbers = input_string.split(" ")

# Declare all used varriable
##
# Amount of numbers in #array_of_numbers
amount_of_numbers = len(array_of_numbers)

##
# Sum of all numbers in #array_of_numbers
sum_of_numbers = 0.0

##
# Mean of all the numbers in #array_of_numbers
mean_of_numbers = 0.0

##
# Sum of \f$ x_{i}\f$ squared and #mean_of_number squared
sum_of_squared_difference = 0.0

##
# Final value
standard_deviation = 0.0

##
# Difference of \f$ x_{i} \f$ and \f$ \overline{x}\f$
difference_of_element = 0.0

##
# Square of #difference_of_element
square_of_difference_of_element = 0.0
variance = 0.0

# Summary of all the elements enetered
for number_string in array_of_numbers:
    if number_string.isdigit():
        sum_of_numbers = math_lib.summary(float(number_string), sum_of_numbers)

# Mean of elements
mean_of_numbers = math_lib.division(sum_of_numbers, amount_of_numbers)

# Summary of difference of each element with average
for number_string in array_of_numbers:
    if number_string.isdigit():
        difference_of_element = math_lib.subtraction(float(number_string), mean_of_numbers)
        square_of_difference_of_element = math_lib.nth_power(difference_of_element, 2)
        sum_of_squared_difference = math_lib.summary(sum_of_squared_difference, square_of_difference_of_element)

# Last counting, I promise:)
variance = math_lib.division(sum_of_squared_difference, amount_of_numbers)
standard_deviation = math_lib.nth_root(2, variance)

print(standard_deviation)
