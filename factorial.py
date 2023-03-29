# Create a function called calculateFactorial() that returns the factorial of its input

r = int(input("Enter your number:"))

def calculatefactorial(r):
    total = 1
    for i in range(1, r + 1):
        total = total * i
    return total
print(calculatefactorial(r))