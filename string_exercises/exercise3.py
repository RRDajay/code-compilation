# Exercise Question 3: Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

def mix_string(s1, s2):
    return first_letter(s1) + first_letter(s2) + middle_letter(s1) + middle_letter(s2) + last_letter(s1) + last_letter(s2)

def first_letter(string):
    return string[0]

def middle_letter(string):
    return string[int (len(string) / 2)]

def last_letter(string):
    return string[-1]
    
s1 = 'America'
s2 = 'Japan'

mix_string(s1, s2)

