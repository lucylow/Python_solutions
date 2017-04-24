#  Complementary DNA sequencing 

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 


def DNA_strand(dna): 
    
    ansarr = []
    for i in dna:
        if i == "A":
            i = "T"
        elif i == "T":
            i = "A"
        elif i == "C":
            i = "G"
        else:
            i = "C"
        ansarr.append(i)
    
    ans = "".join(ansarr)   
    return ans 


def DNA_strand(dna):

    dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([dict[symbol] for symbol in dna])
