# Using List and Loop
# Initializing three numbers
numbers = [10, 20, 30]

# Variable to store sum
sum_numbers = 0

# Calculating sum
for i in numbers:
    sum_numbers += i

# Calculating average
average = sum_numbers / len(numbers)

# Displaying the result
print(f'Sum: {sum_numbers}, Average: {average}')
