# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

def largestperfectsquare(n):
	# your code goes here
	x=2
	r=0
	while(n>=r):
		# print(x**2)
		s=x**2
		# print(s)
		r=s
		if(r==n):
			return r
		if(r>n):
			x=x-1
			return x**2
		x+=1
	
	

print(largestperfectsquare(26))