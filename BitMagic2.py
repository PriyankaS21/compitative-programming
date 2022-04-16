'''
Title: Bit Magic
Description: Trick to cover the binary representation of a number
1. Power of 2
2. one's in Binary Representation of Number
3. Find single occuring element in an array
'''
'''
ispowerof 2
n -> input
True/False -> output
check if n is a powerof 2
512 -> True 512 = 2**9
1024 -> True 1024 = 2**10
'''

def ispowerof2(n):
    # T.C = O(1)
    if n < 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y

# return's number of 1's in binary representation of int
# 5 -> 101 ans = 2
# 7 -> 111 ans = 3

def bruteforce(n):
    # T.C = O(n)
    s = str(bin(n))[2:]
    print("{}".format(s))
    return s.count('1')

def cntnits(n):
    # T.C = O(logn)
    cnt = 0
    while n:
        cnt+=1
        n = n & (n-1)
    return cnt

t = int(input())
while t:
    n = int(input())
    # print(ispowerof2(n))
    print(bruteforce(n))
    print(cntnits(n))
    t = t-1