# Exercise Question 5: Count all lower case, upper case, digits, and special symbols from a given string

def findDigitsCharsSymbols(string):

    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in string:
        if char.isalpha():
            char_count += 1
        
        elif char.isdigit():
            digit_count += 1

        else:
            symbol_count += 1

    print(f'Chars:{char_count}\nDigits:{digit_count}\nSymbols:{symbol_count}')


str1 = "P@#yn26at^&i5ve"

findDigitsCharsSymbols(str1)