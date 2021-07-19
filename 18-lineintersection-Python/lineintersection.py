# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	if(m1==m2 or b1==b2):
		return None
	# elif(ismultiple(m1,m2) or ismultiple(m2,m1)):
	# 	return None
	else:
		r=(b2-b1)/(m1-m2)
		# print(r)
		if(r<=1):
			return None
		return int(r)
	# your code goes here
	# return ""


print(lineintersection(8, 13, 4, 17))