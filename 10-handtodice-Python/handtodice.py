# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	
	t=[]
	s=str(hand)

	for i in s:
		t.append(int(i))

	# print(tuple(t))
	return tuple(t)
	
	# l=[]

	# while(hand>0):
	# 	s=hand%10
	# 	# print(s)
	# 	hand=hand//10
	# 	#print(hand)
	# 	l.insert(0,s)
		
	# # print(tuple(l))



	# return tuple(l)
	# your code goes here

handtodice(101)
