import re

# Open and read the file
with open("regex_sum_2171642.txt") as file:  # Make sure the filename matches your downloaded file
    data = file.read()

# Find all numbers in the file
numbers = re.findall(r'[0-9]+', data)

# Convert strings to integers and sum them up
total_sum = sum(map(int, numbers))

# Print the final sum
print("Sum of numbers:", total_sum)
