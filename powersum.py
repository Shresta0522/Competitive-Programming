# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.
import pytest
def powerSum(n, k):
    # Your code goes here...
    s=0
    if(n<=0) or k<=0:
        return 0
    else:
        for i in range(1,n+1):
            # print(i)
            s=s+i**k
        # print(s)
        return s
# Write your own test cases here...
@pytest.mark.parametrize('n,k,s',[
    (0,0,0),(-1,1,0),(1,-1,0),(2,2,5)
])

def test(n,k,s):
    assert powerSum(n,k)==s

print ("All test cases passed...")

# print(powerSum(2,2))