# We can determine how many digits a positive integer has by
# repeatedly dividing by 10 (without keeping the remainder) until the
# number is less than 10, consisting of only 1 digit. We add 1 to this
# value for each time we divided by 10. Here is the recursive
# algorithm: 

# def numberOfDigits(num):

#     if num / 