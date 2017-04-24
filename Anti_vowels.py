
# Remove all the vowels from a string input 

def anti_vowel(text):
    ans = ""
    
    for char in text:
        # if char in "aeiouAEIOU":
        #     ans += ""
        # else:
        #     ans += char
        if char not in "aeiouAEIOU":
            ans += char
            
    return ans
            
anti_vowel("Hey You!")
