#!/usr/bin/env python3

def mendel_pair(k, m, n):
    t = k + m + n
    return 1 - (1/(t*(t-1)))*(0.25*m*(m-1) + m*n + n*(n-1))

if __name__ == '__main__':
    print(mendel_pair(2, 2, 2))
