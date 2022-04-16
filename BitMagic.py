'''
Title: Bit Magic
Description: Tricks to cover the binary representation of a number


bitwise operator and - &
bitwise operator or - |
bitwise operator not - ~
bitwise operator xor - ^
bitwise operator right shift - >>
bitwise operator left shift - <<

right shift is divide in power of 2
left shift is multiply in power of 2
'''
''' 
Samples Cases for &
2 & 1
>>>0
4 & 1
>>>0

500 & 1
>>>0

3 & 1
>>>1

5 & 1
>>>1

Samples Cases for >>
n = 32
n >> 2
>>>8

n << 2
>>>128

m = 200
m >> 3
>>>25   # m = 200 // 2**3 = 200 // 8 = 25

m << 4 # 400 * (2**4) = 400 * 16 = 6400
'''
def evenodd(n):
    if n&1 == 1:
        print("odd")
    else:
        print("even")

def mulpow2(x, y):
    return x << y

def divpow2(x,y):
    return x >> y
t = int(input())
while t:
    # n = int(input())    
    # evenodd(n)
    x,y = map(int,input().split())
    print(mulpow2(x,y))
    print(divpow2(x,y))
    t = t-1

