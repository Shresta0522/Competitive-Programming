
import math
def test(k):
    r=0
    for i in range(k):
        d=math.pow(2,i)
        r=r+(1/d)
        print("r",r)
    return r

print(test(2))