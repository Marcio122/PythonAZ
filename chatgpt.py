# Real-life example: Printing multiples of a number up to a certain limit

# Define the number whose multiples we want to print
number = 5

# Define the limit up to which we want to print multiples
limit = 50

# Iterate through numbers from 1 to the limit
for i in range(1, limit + 1):
    # Check if the current number is a multiple of 'number'
    if i % number == 0:
        print(i, "is a multiple of", number)
