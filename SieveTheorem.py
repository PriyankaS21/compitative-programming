'''
Topic: Very Important Seive Theorem
Description: Generate All primes upto N in T.C O(n*log(logn))
0 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32 33 34 35 36 37 38 39 40
41 42 43 44 45 46 47 48 49 50


So we are going to generate all the prime no till no 50

Basic approach:
for each number from 1 to N: O(N)
    traverse and check for every number if it is a prime ---> chcek prime sqrtroot(N):
        you will print O(1) constant

T.C = N*root(N)

what we are going to do:
-> we will take all the no till 50 in list
-> exclude 0 and 1, coz prime no starts with 2
-> remove the greater and equal sqr of 2 no, 
-> repeat the last task with 3
-> repeat for 4 and 5 and so on

'''

from math import *

def generatePrime(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2, int(sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False
    
    for i in range(0, len(primes)):
        if primes[i] == True:
            print(i, end = " ")


t =  int(input())
while t:
    n = int(input())
    generatePrime(n)
    t = t-1



