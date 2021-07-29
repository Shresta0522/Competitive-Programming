# matrixAdd(L, M)[10 pts]
# Background: we can think of a 2d list in Python as a matrix in math. To add two matrices, L and M, they must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For example:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matrixAdd(L, M) == N)
# With this in mind, write the function matrixAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that you 
# may assume only contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because they are of different dimensions.

def matrixadd(L, M):
	# Your code goes here
	if((len(L))!=(len(M)) or (len(L)==0 or len(M)==0)):
		return None
	r=len(L)
	c=len(L[0])

	
	m = [ [ 0 for i in range(c) ] for j in range(r) ]
	# print(m)
	for i in range(r):
		if(len(L[i])!=len(M[i])):
			return None

		for j in range(c):
		# 	print(L[i][j],M[i][j])
			m[i][j]=L[i][j]+M[i][j]

		# print(m)
	return m

# print(matrixadd([[1,  2,  3],[4,  5,  6]], [[21, 22, 23], [24, 25]]))