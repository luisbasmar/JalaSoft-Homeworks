# Fn = Fn-1 + Fn-2.
def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n

print(rec_fib(5))