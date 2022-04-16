# Sum of n natural numbers

def sum1(n):
    # O(1)
    return (n)*(n+1) //2

def sum2(n):
    # O(n)
    sm = 0
    for i in range(1,n+1): # [1, n]
        sm = sm + i
    return sm

t = int(input())
while t: # t = test case, in short we are telling how many test cases
    n = int(input())
    print("Sum1 executed output {}".format(sum1(n)))
    print("Sum1 executed output {}".format(sum2(n)))

    t = t-1

''' Sample Output
3
5
Sum1 executed output 15
Sum1 executed output 15
10
Sum1 executed output 55
Sum1 executed output 55
1002665412365651321
Sum1 executed output 502668964577190804986992402457348181
'''

'''
Thus, O(n) > O(1), always try to avoid loops
'''

