# Exercise Question 4: Arrange string characters such that lowercase letters should come first

def find_uppercase(string):
    uppercase = ''
    for char in string:
        if char.isupper():
            uppercase += char

    return uppercase

def find_lowercase(string):
    lowercase = ''
    for char in string:
        if char.islower():
            lowercase += char

    return lowercase
    
def arrange_string(string):
    
    return find_lowercase(string) + find_uppercase(string)

str1 = "PyNaTive"

arrange_string(str1)



