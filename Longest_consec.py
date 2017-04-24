'''
Given an array strarr of strings and an integer k, the function returns the first longest string consisting of k consecutive strings taken in the array.

Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

'''



def longest_consec(strarr, k):
    leng = len(strarr)
    if leng == 0 or k > leng or k <= 0: return ""
    ans_arr = []
    
    # first step to get the lengths of each index's and the following k - 1 elements
    for ind in xrange(0, leng - (k - 1)):
        total_len = 0
        for cur_ind in xrange(ind, ind + k):
            cur_word = strarr[cur_ind]
            total_len += len(cur_word)
        ans_arr.append(total_len)
    
    # now, you check in the ans_arr which index has the largest index,and you keep the index
    ans_ind = -1 # this is just another way of saying i don't have an index yet instead of defaulting it to 0
    cur_longest_leng = -1 # same idea here
    for i, cur_consecutive_leng in enumerate(ans_arr): # enumerate is awesome, it gives you the index AND the item as you loop. Learn to use this frequently
        if cur_consecutive_leng > cur_longest_leng:
            ans_ind = i
            cur_longest_leng = cur_consecutive_leng
    
    # so now you have the index with the answer, now you need to piece the string together
    ans_str = ""
    for i in xrange(ans_ind, ans_ind + k):
        ans_str += strarr[i]
    
    return ans_str
    
