def LongestWord(sen):

    sen = sen.split(" ")

    longest_word = ''

    for word in sen:
        if word.isalpha():
            if len(word) > len(longest_word):
                longest_word = word

        elif word.isdigit():
            if len(word) > len(longest_word):
                longest_word = word
    
    # code goes here
    return longest_word

sen = "123 4567 8975"

# keep this function call here 
print (LongestWord(sen))