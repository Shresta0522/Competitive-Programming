# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]
import itertools
def limitedPowerSet(n, k):
    s=set()
    d=[{}]
    for i in range(1,n+1):
        s.add(i)


    for i in range(1,len(s)+1):
        a=list(map(set,itertools.combinations(s,i)))
        for j in range(len(a)):
            if(len(d)!=k):
                d.append(a[j])
            else:
                return d
    # if(n==k+1):
    # for i in range(n):
    #     if(len(d)==k):
    #         return d
    #     d.append({i+1})
    # # Your code goes here...
    # print(d)
    # return d
    # else:

    # for i in range(d):
print(limitedPowerSet(5,7))
