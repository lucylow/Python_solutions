
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

'''

#my attempt
def isAanagram(s,t):
	s, t = s.split(), t.split()
	if sorted(s) ==sorted(t):
		return True
	else:
		return False

# simple not effective
def isAnagram(s, t):
        return sorted(s) == sorted(t)

#creative 

def isAanagram(s, t):
	return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')


#other
def isAnagram(s, t):
        if set(s) != set(t):
            return False
        else:
            for  element in set(s):
                if s.count(element) != t.count(element):
                    return False
            return True
