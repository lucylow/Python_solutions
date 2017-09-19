def str_checker(s):
	dic = {}

	for letter in s:
		if letter not in dic:
			dic[letter] = 1 
		else:
			return False 
	return True 
