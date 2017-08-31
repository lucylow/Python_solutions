'''
When given a string of space separated words, return the word with the longest length. If there are multiple words with the longest length, return the last instance of the word with the longest length.

Example:

'red white blue' //returns string value of white

'red blue gold' //returns gold

'''

def longest_word(s):
    return sorted(s.split(), key = len)[-1]
    
    
def longest_word(words):
    return max(reversed(words.split()), key=len)
