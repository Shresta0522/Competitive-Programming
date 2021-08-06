# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    # Your code goes here...
    if(data==""):
        return None

    d=data.split("\n")[0:-1]
    # print(d)
    
    names=[]
    scores=[]
    for i in (d):
        s=i.split(",")
        # score=score+s[]
        names.append(s[0])
        s.remove(s[0])
        p=0
        for i in s:
            # print(i)
            p=p+int(i)
        # print(p)
        scores.append(p)
        # p=p+int(s[i])
        # print(p)
    if(scores[0]==scores[1]):
        return names[0]+","+names[1] 
    elif(scores[0]==max(scores)):
        return names[0]
    else:
        return names[1]
    
        
    

print()

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
# print(topScorer(data))
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
# print(topScorer(data))
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
