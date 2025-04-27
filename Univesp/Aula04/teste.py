def fib_it(n):
    res = n
    a,b = 0,1
    for k in range(2, n+1):
        res = a + b
        a,b = b, res
    return res

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)
    
start = time.time()
print(fib_rec(1500))
