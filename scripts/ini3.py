#!/usr/bin/env python3


def index_string(s, a, b, c, d):
    """Return 2 strings from s corresponding to characters a-b and c-d."""
    outstring1 = s[a:b+1]
    outstring2 = s[c:d+1]
    return outstring1, outstring2

s = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'

mylist = [1, 2, 3, 4, 5, 6, 100, 'hello']

print(index_string(s, 22, 27, 97, 102))


