
# Censorship and strings

def censor(text, word): # word all lower cases, and no punctuation
    # text will censor your word of choice with asterisks
    
    ans = []
    
    censor = "*" * len(word) 
    for wordsplit in text.split():
        if wordsplit == word:
            
            ans.append(censor) 
        else:
            ans.append(wordsplit)
    
    return " ".join(ans)
    
    
#censor("hey hey hey","hey")
