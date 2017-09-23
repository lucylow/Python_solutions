
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

'''

def anagram(s1, s2):
	dic1 = {}
	for i in s1:
		if i not in dic1:
			dic1[i] = 1 
		else:
			dic1[i] += 1
	for i in s2:
		if i not in dic1 or dic1[i] == 0:
			return False
		else:
			dic1[i] -= 1
	return True
