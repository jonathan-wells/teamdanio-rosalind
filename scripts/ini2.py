#!/usr/bin/env python3

def hypotenuse(a, b):
    """Return the hypotensuse of a triangle with base a and height b."""
    c = (a**2 + b**2)**0.5
    return c

a = 3
for b in range(0, 100):
    c = hypotenuse(a, b)
    print(a, b, c)

if a == 5:
    print(hypotenuse(a, 10))
else:
    print('nope')
