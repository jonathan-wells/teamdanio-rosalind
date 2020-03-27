#!/usr/bin/env python3

def isodd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def oddsum(a, b):
    oddlist = []
    for i in range(a, b+1):
        if isodd(i) == True:
            oddlist.append(i)
    return sum(oddlist)

def oddsum_short(a, b):
    return sum([i for i in range(a, b+1) if i % 2 == 1])


mylist = [0, 1, 2, 3]
a = 0
b = 3

print(oddsum(a, b))
print(oddsum_short(a, b))

## Below are examples of the difference between 'while' and 'for' loops
# for i in range(10):
#     print(i)

# i = 0
# while i < 10:
#     print(i)
#     i += 1

