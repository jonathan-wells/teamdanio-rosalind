#!/usr/bin/env python3

def fib_rec(n):
    if n < 0:
        raise ValueError('n must be positive')
    elif n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

def fib_fast(n):
    if n < 0:
        raise ValueError('n must be positive')
    
    fibseq = [0, 1, 1]
    for i in range(2, n):
        fibseq.append(fibseq[-1] + fibseq[-2])
    
    return fibseq[n]

def rabbits(n, k):
    if n < 0:
        raise ValueError('n must be positive')
    
    rabseq = [0, 1, 1]
    for i in range(2, n):
        rabseq.append(rabseq[-1] + k*rabseq[-2])
    return rabseq[n]

if __name__ == "__main__":
    # for i in range(30):
    #     assert fib_fast(i) == fib_rec(i)
    print(rabbits(5, 3))
    print(fib_fast(7))
