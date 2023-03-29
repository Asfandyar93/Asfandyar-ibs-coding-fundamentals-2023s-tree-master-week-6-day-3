# Create a function named isAnagram() following your current language's style guide.
# It should take two strings and return a boolean value depending on whether it's an anagram or not.

a = "two"
b= "tow"
def is_anagram(a,b):
    flag = 0
    for i in a:
        for j in b:
            if i == j:
                flag = flag + 1
                break
    if flag == len(a):
        return True
    else:
        return False
print(is_anagram(a,b))
