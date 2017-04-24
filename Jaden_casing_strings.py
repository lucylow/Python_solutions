
# Jaden Casing Strings

# Jaden Smith capitalizes every word on Twitter 

def toJadenCase(string):
    ans = []
    string = string.split(" ")
    for word in string:
        word = word[0].upper() + word[1:] # word.capitalize() works too 
        ans.append(word)
        
    ans = " ".join(ans)
    return ans 


quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(toJadenCase(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")

