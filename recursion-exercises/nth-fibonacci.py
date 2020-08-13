# Write a method to generate the nth Fibonacci number.

# 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibonacci(n_th, prev_num=0, present_num=1, counter=1):
    
    next_num = present_num + prev_num

    if n_th == 0:
        print(f'f({counter-1}) = {prev_num}')
        return prev_num

    if counter == n_th:
        print(f'f({counter}) = {present_num}')
        return present_num 

    else:
        fibonacci(n_th, present_num, next_num, counter+1)

for _ in range(10):
    fibonacci(_) 