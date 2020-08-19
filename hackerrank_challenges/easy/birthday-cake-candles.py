def birthdayCakeCandles(ar):
    n = max(ar)
    number_of_candles = 0

    for num in ar:
        if num == n:
            number_of_candles +=1

    return number_of_candles

    arr = [3,2,1,3]

    birthdayCakeCandles(arr)