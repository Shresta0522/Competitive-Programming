# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(n):
    # Your code goes here
    if(n==1):
        return True

    if(prime(n)):
        s=sum_digits(n)
        if(s<9 and s==1):
            return True
        else:
            while(s>9):
                print("s",s)
                s=sum_digits(s)
    
            if(s==1):
                return True
            else:
                return False
    else:
        return False

def prime(n):
    if(n<=1):
        return False
    elif(n==2 or n==3):
        return True
    elif(n%2==0):
        return False
    else:
        for i in range(3,n):
            if(n%i==0):
                return False
        return True

print(prime(833))
def sum_digits(n):
    s=0
    while(n>0):
        a=n%10
        s=s+(a**2)
        # print("s",s)
        n=n//10
        # print("n",n)
        # print(a)
        
    return s
# print(sum_digits(13))

print(ishappyprimenumber(383))