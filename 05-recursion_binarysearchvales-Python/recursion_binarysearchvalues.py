# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list 
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an 
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0 
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we 
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2 
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We 
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L. 
import pytest
r=[]

def binarysearch_value(L,low,high,v):
	# r=[]
	if(high>=low):
		m=low+(high-low)//2
		if (L[m]==v):
			a=(m,L[m])
			# print(a)
			r.append(a)
			# print("r",r)
			return r
		elif (L[m]>v):
			a=(m,L[m])
			# print(a)
			r.append(a)
			# print("r",r)
			return binarysearch_value(L,low,m-1,v)
		else:
			a=(m,L[m])
			# print(a)
			r.append(a)
			# print("r",r)
			return binarysearch_value(L,m+1,high,v)
	else:
		# r=[]
		return r

def recursion_binarysearchvalues(L, v):
	
	
	r.clear()
	result=binarysearch_value(L,0,len(L)-1,v)
	# print(result)
	return result

	# Your codes goes here


assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'q') == [(2,'f'), (4, 'm'), (5, 'q')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'a')== [(2,'f'), (0,'a')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'],'c')== [(2,'f'), (0,'a'), (1,'c')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'],'f')== [(2,'f')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'g') == [(2,'f'), (4, 'm'), (3, 'g')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'm') ==  [(2,'f'), (4, 'm')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'z') == [(2,'f'), (4, 'm'), (5, 'q')]
assert recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'b') == [(2,'f'), (0,'a'), (1,'c')]

print("All testcases passed....")
# print(recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'],'q'))