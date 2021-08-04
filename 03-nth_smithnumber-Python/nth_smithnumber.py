# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def sum(n):
    s=0
    while(n!=0):
        s=s+n%10
        n=n//10     
    # print(s)
    return s

# print("Sum function",sum(378))

def prime(n):
    s=0
    if(n<=1):
        return False
    elif(n==2 or n==3):
        return False
    
    else:
    
        for i in range(2,n):
            while(n%i==0):
                if(i<9):
                    s=s+i
                else:
                    # print("##")
                    # print(sum(i))
                    d=(sum(i))
                    s=s+d

                # print(i)
                n=n/i
        # print("s",s)

        #     if(n%i==0):
        #         return False
        return s
# 
# print(prime(58))


# print(sum())

def smithnumber(n):
    return (sum(n)==prime(n))


# print(smithnumber())      


def fun_nth_smithnumber(n):
    count=0
    i=1

    # print(smithnumber(i))
    while(True):
        if(smithnumber(i)):
            if(count==n):
                return i
            count+=1
        i+=1

    
# print(fun_nth_smithnumber(19))




    