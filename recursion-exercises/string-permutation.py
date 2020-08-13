# Write a method to compute all permutations of a string.

# Example for ABC: ABC ACB BAC BCA CBA CAB

def permutations(s):

    if len(s) <= 1:
        return [s]

    else:
        list_of_permutations = []
        for elements in permutations(s[:-1]):

            for i in range(len(elements)+1):
                list_of_permutations.append(elements[:i] + s[-1] + elements[i:])

        return list_of_permutations

string = 'ABC'

print(permutations(string))






