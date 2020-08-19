def compareTriplets(a, b):

    a_score, b_score = 0, 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a_score+=1
        elif a[i] < b[i]:
            b_score+=1
        else:
            pass
        
    return [a_score, b_score]

a = [5,6,7]
b = [3,6,10]

compareTriplets(a,b)