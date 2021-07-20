# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	
	d=0
	col=0
	for i in range(len(a)):
		r=0
		c=0
		# print(a[i])
		for j in range(len(a[i])):
			# print("j",j)
			r+=a[i][j]
			# print("value",a[j][i])
			c+=a[j][i]
		# print("c",c)
			if(i==j):
				# print("d",a[j][j])
				d+=a[j][j]
			# print("CC",c)
		# print("j",j)
			
		if(i==0):
			row=r
			# print("r")
		else:
			if(row!=r):
				return False

		# print("r",r)
		# col=c
		# if(col!=c):
		# 	return False

		# print("c",c)
	# print("d",d)

	if(r==c) and(r==d) :
		return True
	else:
		return False
	# Your code goes here
	# return a 

print(ismostlymagicsquare([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))