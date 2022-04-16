#GCD and LCM

#euclid also
# T.C = o(log(min(a,b)))
# product = lcm * gcd
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    prod = a* b
    hcf  = gcd(a,b)
    return prod // hcf

t = int(input())
while t:
    n,m = map(int,input().split())
    print("gcd = {} lcm = {}".format(gcd(n,m),lcm(n,m)))
    t = t-1


''' Sample Output
1
5 10
gcd = 5 lcm = 10

C:\Users\psingh410\OneDrive - DXC Production\Competative Programming>C:/Python/python.exe "c:/Users/psingh410/OneDrive - DXC Production/Competative Programming/gcdandlcm.py"
2
5 10
gcd = 5 lcm = 10
20 50
gcd = 10 lcm = 100
'''
