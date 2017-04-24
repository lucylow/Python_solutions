# Calculate Scrabble Score


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         # dictinoary w string --> integer 
         
         
         
# given string, return the scrabble score for that word 

def scrabble_score(word): # word has is non-empty and has no spaces, or punctuation 

    ans = 0
    
    for letter in word:
        for key in score:
            if key.upper() == letter or key.lower() == letter:
                ans += score[key]
    
    return ans
