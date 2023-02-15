# # Input a number
# a = 1.23456789
#
# # Round the number to 3 decimal places
# rounded_number = round(a, 3)
#
# # Convert the rounded number to a string
# string_number = str(rounded_number)
#
# # Output the string number
# print(string_number)

# Input a number
a = 1.23456789

# Multiply the number by 1000 to move the decimal point 3 places to the right
b = a * 1000

# Round the number to the nearest integer using the round() function
# if b % 1 >= 0.5:
#     rounded_number = round(b)
# else:
#     rounded_number = round(b - 1)
#
# # Divide the rounded number by 1000 to move the decimal point 3 places to the left
# c = rounded_number / 1000
#
# # Convert the rounded number to a string
# string_number = str(c)
#
# # Output the string number
# print(string_number)

# Input a number
a = 1.23456789

# Format the number to display only 3 decimal places using %
formatted_number = "%.3f" % a

# Output the formatted number
print(formatted_number)

