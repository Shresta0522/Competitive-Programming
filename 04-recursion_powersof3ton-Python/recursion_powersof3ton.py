# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def recursion_powersof3ton(n):
	# Your code goes here
	l=[]
	if(n<1):
		return None
	else:
		return powerof3ton(l,n,0)

	

def powerof3ton(l,n,p):
	# print(p)
	power=3**p
	if(p>=(n-1)):
		l.append(power)
		return l
	else:
		p+=1
		l.append(power)
		# print(l)
		return powerof3ton(l,n,p)


print(recursion_powersof3ton(4))
