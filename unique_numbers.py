# Create a function that takes a list of numbers as a parameter and
# returns a list of numbers where every number is unique (occurs only once)

m = [1,2,2,1,2,3,3,4,5,6,7,8,9]

def unique_numbers(m):
    o = []
    o.append(m[0])
    for i, val in enumerate(m):
        if len(matching_index(val, o)) == 0:
            o.append(val)
    return o
print(unique_numbers(m))

