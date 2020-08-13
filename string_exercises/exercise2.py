# Exercise Question 2: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
def appendMiddle(s1, s2):
    middleIndex = int (len(s1) / 2)

    return s1[:middleIndex] + s2 + s1[middleIndex:]

s1 = "Ault"
s2 = "Kelly"

print(appendMiddle(s1, s2))


