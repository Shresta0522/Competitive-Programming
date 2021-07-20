# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


def nthpowerfulnumber(n):
	count=1
	if(n==0):
		return 1
	else:
		count=-1
		i=1
		while(n>count):
			if(powerfulnumber(i)):
				# print(i)
				count+=1
			i+=1
		return i-1


	# Your code goes here
	# return None

def powerfulnumber(n):
	for i in range(1,n+1):
		if(n%i==0):
			# print(i)
			if(primenumber(i)):
				# print(i)
				if((n%(i**2))!=0):
					return False
	
	return True

def primenumber(k):
	if(k<2):
		return False
	elif(k==2):
		return True
	elif(k%2==0):
		return False
	else:
		for i in range(3,k):
			# print(k,i)
			if((k%i)==0):
				return False
			
		return True

# print(primenumber(35))
# print(powerfulnumber(35))


print(nthpowerfulnumber(5))