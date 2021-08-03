# Recursion-Only recursion_secondlargest(L) [15 pts]
# Note: recall that you may not use sort, sorted, min, or max this week! With that in mind, write the function 
# recursion_secondlargest(L) that takes a list of integers in any order and returns the second-largest value in the list. To 
# be more precise, it returns the second value from the end if the list was sorted (though you do not need to sort 
# it to solve this problem), so if the largest value occurs twice, you would return that value. Also, if there are 
# fewer than 2 values in the list, return None. Here are some test cases:
# assert(recursion_secondlargest([1,2,3,4,5]) == 4)
# assert(recursion_secondlargest([4,3]) == 3)
# assert(recursion_secondlargest([4,4,3]) == 4)
# assert(recursion_secondlargest([-3,-4]) == -4)
# assert(recursion_secondlargest([4]) == None)
# assert(recursion_secondlargest([ ]) == None)
# Again, you do not need to sort the list. We didn't sort it in our sample solution. We just tracked the two largest 
# values as we recursively traversed the list. Also, you may not use loops/iteration in this problem
c=0	
def secondlargest(L,m):
	global c
	# print(L)
	m=max(L)
	# print(m)
	c+=1
	# print("C",c)
	if(L.count(m)>=2):
		return m
	if(c==2):
		c=0
		# print(c)
		return m
	if(c<2):
		# print("####")
		# print(m)
		L.remove(m)
		# 
		return secondlargest(L,0)

def recursion_secondlargest(L):
	# Your code goes here
	global c
	c=0
	m=0
	# print("r",len(L))
	# print("g",L)
	if(len(L)<=1):
		return None
	return secondlargest(L,m)


	

assert recursion_secondlargest([4,4,3])==4
assert recursion_secondlargest([-3,-4])==-4
print("passed")
print(recursion_secondlargest([-3,-4]))
# print(recursion_secondlargest([4]))