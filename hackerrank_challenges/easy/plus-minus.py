def plusMinus(arr):

    pos_count, neg_count, zero_count = 0, 0, 0
    n = len(arr)

    for num in arr:

        if num > 0:
            pos_count += 1

        elif num < 0:
            neg_count += 1

        else:
            zero_count += 1

    print(f"{pos_count/n}\n{neg_count/n}\n{zero_count/n}")

arr = [-4, 3, -9, 0, 4, 1]
print(plusMinus(arr))