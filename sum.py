# Write a function called sum() that returns the sum of numbers from zero to the given parameter

def sum(input_value):
    total = 0
    for i in range(0, input_value + 1):
        total = total + i
    return total
print(sum(11))