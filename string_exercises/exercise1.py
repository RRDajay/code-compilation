# Exercise Question 1: Given a string of odd length greater 7, 
# return a string made of the middle three chars of a given String

def is_odd(string):
    
    str_length = len(string)
    mod = str_length % 2

    if mod > 0:
        return True

    else:
        return False

def getMiddleThreeChars(string):

    if is_odd(string) and len(string) >= 7:
        return string[(int(len(string)/2)-1):(int(len(string)/2)+2)]

    else:
        return False

str1 = "JhonDipPeta"
str2 = "JaSonAy"

print(getMiddleThreeChars(str1))
print(getMiddleThreeChars(str2))