def fun(n):
    if n == 0: 
        return 0

    return n + fun(n-1)
    
total = fun(5)
print(total)