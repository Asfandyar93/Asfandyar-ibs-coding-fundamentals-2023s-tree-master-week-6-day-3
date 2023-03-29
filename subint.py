# Create a function that takes a number and
# a list of numbers as a parameter and returns the indexes of the numbers of the list
# which contain the given number or returns an empty list
# (if the number is not part of, any of the numbers in the list)

n = 2
m = [1,2,3,4,4,2,1,2,3,2]

def matching_index(n,m):
    o = []
    for i in range(1):
        for j, val in enumerate(m):
            if n == val:
                o.append(j)
    return o

print(matching_index(2,[1,2,3,4,4,2,1,2,3,2]))

m = [4,5,6]
n = 4
o = []

[0]

m = [4,5,4,4,4,6]
n = [4]
o = []

[0,2,3,4]