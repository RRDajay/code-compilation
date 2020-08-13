# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
# For example: if the input string is "Hello World and Coders" then your program should return the string 
# sredoC dna dlroW olleH.

def FirstReverse(string):

    reversed_string = ''

    for char in reversed(string):
        reversed_string += char

    return reversed_string

string = 'I Love Code'
print(FirstReverse(string))