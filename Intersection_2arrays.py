# find the intersection of two arrays 
# [1,2,3] == [3,4,5] ==> [3]
# [2,2,2] , [2,2,4] ==> [2,2]



def str_checker(s1, s2):
	answer = []
	dic = {}

	for char in s1:
		if char not in dic:
			dic[char] = 1
		else:
			dic[char] += 1

	for char in s2:
		if char in dic and dic[char] > 0:
			dic[char] -= 1
			answer.append(char)
	return answer 


def stcheck(s1, s2):
	#two dictionaries 
	bd1 = {}
	bd2 = {}
	ans = []
	for char in s1:
		if char in bd1:
			bd1[char] += 1
		else:
			bd1[char] = 1
	for _char in s2:
		if _char in bd2:
			bd2[_char] += 1
		else:
			bd2[_char] = 1
	
	for let in bd1.keys():
		if let in bd2:
			ans.append(let * min(bd1[let], bd2[let]))
	
	return ans
