# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	s=math.sqrt((b**2)-(4*a*c))
	x=-(b+s)/2*a
	y=-(b-s)/2*a
	return int(x),int(y)


# print(fun_find_int_roots(1, -5, 6))