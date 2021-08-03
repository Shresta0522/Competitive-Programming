# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	count=1
	if(n==0):
		return 0
	else:
		i=1
		while (True):
			s=pronic(i)
			if(n==count):
				return s
			count+=1
			i+=1


	# Your code goes here

def pronic(n):
	n=abs(n)
	return n*(n+1)

print(nthpronicnumber(7))
