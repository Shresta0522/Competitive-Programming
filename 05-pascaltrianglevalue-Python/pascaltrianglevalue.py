# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


import math

def ncrfact(n,r):
	nfact = math.factorial(n)
	rfact = math.factorial(r)
	return nfact/(rfact*(math.factorial(n-r)))


def fun_pascaltrianglevalue(row, col):
	if (row>=0) and (col>=0):
		if col<=row:
			r = ncrfact(row,col)
			# print(r)
			return int(r)
		else:
			return 0
# print(fun_pascaltrianglevalue(4,2))