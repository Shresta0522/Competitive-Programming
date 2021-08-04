# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def withproperty309(n):
	digit=str(n**5)
	numb=[0,1,2,3,4,5,6,7,8,9]

	for i in numb:
		if(str(i) not in digit):
			return False
	return True

def nthwithproperty309(n):
	# Your code goes here5
	count=0
	i=1
	while(True):
		if(withproperty309(i)):
			if(count==n):
				return i
			count+=1
		i+=1

print(nthwithproperty309(6))