# purify removes all ODD numbers in the list
# purify[1,2,3] --> [2]

def purify(lst): #lst = list of numbers 
    ans = []
    
    for i in lst:
        if i % 2 == 0:
            ans.append(i)
            
    return ans
