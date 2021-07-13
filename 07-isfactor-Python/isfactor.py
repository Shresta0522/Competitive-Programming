# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.

# (f%n)==0) and  f==0 or

def fun_isfactor(f, n):
	f=abs(f)
	# print(f%n)
	

	if( n==0 or (f==0 and n==0)):
		return True

	if(f==0):
		return False
	else:
		if(f>n):
			if (f%n==0) :
				return True
			else:
				return False # replace with your solution
		else:
			if (n%f==0) :
				return True
			else:
				return False
print(fun_isfactor(-2,4))