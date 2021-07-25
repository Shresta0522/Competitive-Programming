
def prime(n):
    if(n<1):
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


def sum(n):
    z=0
    while(n>0):
        a=n%10
        n=n//10
        # print("a",n%10)
        # print("b",n//10)
        z+=a
			
    # print("z",z)
    return z


# print(sum(29))





def isAdditivePrime(n):
    # print("nn",n)
    if(n<=9):
        if(prime(n)):
            return True
        return False
    else:
        # print(n)
        s=sum(n)
        # print("s",s)
        return isAdditivePrime(s)



print(isAdditivePrime(97))


# print(prime(11))
