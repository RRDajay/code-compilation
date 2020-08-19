def staircase(n):
    
    space, hashtg = ' ', '#'

    for i in range(n):
        print(space*(n-1-i) + hashtg*(i+1))

staircase(6)