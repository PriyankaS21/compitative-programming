'''
Title: Number Theory 3 Primility Test
Description: Comparing Primility Test in O(n) vs O(root(n))
'''

# Primr Number two factors 1, Number Itself
#approach One O(n)
# Approach Two: Base Case + Hint: O(1) -> O(root(N))
from math import *
def approach1(n):
    divcnt = 0
    for i in range(1, n+10): # [1,n]
        if n%i == 0:
            divcnt+=1
    print(divcnt)
    if divcnt == 2:
        return True
    else:
        return False

def approach2(n):
    
    if n == 0 or n == 1: # O(1)
        return False
    if n == 2 or n == 3: # O(1)
        return True
    if n%2 == 0 or n%3 == 0: # O(1)
        return False

    for i in range(5, int(sqrt(n)) + 1): # [1, root n]
        if n%i == 0 or n%(i+2) == 0:
            return False

    return True

t = int(input())
while t:
    n = int(input())
    # print(approach1(n))
    print(approach2(n))
    t = t-1