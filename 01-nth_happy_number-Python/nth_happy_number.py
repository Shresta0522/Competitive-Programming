# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


def nth_happy_number(n):
	if(n==1):
		return 1
	count=1
	i=2
	while(True):
		if(ishappynumber(i)):
			if(count==n):
				return i
			count+=1
		i+=1



	return 0


def ishappynumber(n):
	s=n
	if(n<=0):
			return False
	elif(n==1 or n==6):
		return s
				
	while(n>=1):
		# print("nnn",n)
		if(n==1 or n==6):
			return s
		elif(n==4):
			return False
		else:
			n=sum(n)
	
		# print(z)

def sum(n):
	z=0
	while(n>0):
			a=n%10
			# print("a",n%10)
			# print("b",n//10)
			z+=(a**2)
			n=n//10
	# print("z",z)
	return z
print(nth_happy_number(5))