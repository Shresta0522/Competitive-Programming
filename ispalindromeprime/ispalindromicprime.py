


def prime(n):
    if(n<=0):
        return False
    elif(n<=3):
        return True
    elif(n%2==0):
        return False
    else:
        for i in range(3,n):
            if((n%i)==0):
                return False
        return True

def ispalindromeprime(n):
    s=n
    r=0
    if(prime(n)):
        while(n!=0):
            a=n%10
            # print(a)
            r=r*10+a
            # print("r",r)
            n=n//10
        # print("res",r)
        if(r==s):
            return True
    else:
        return False

# print(isPalindromePrime(182))
