# Create a function that takes a list of numbers as parameter and
# returns a list where the elements are sorted in ascending numerical order When you are done,
# add a second boolean parameter to the function If it is true sort the list descending, otherwise ascending

a = [5,6,9,1,68]
def bubble(a,flag):
    if flag == True:
        for i in range(len(a) - 1, 0, -1):
            for j in range(i):
                if a[j] < a[j + 1]:
                    b = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = b
        return a
    if flag == False:
        for i in range(len(a) - 1, 0, -1):
            for j in range(i):
                if a[j] > a[j + 1]:
                    b = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = b
        return a
print(bubble(a,True))