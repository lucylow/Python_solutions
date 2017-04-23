
#binary 


'''
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
'''





#bit-mask 

def check_bit4(input):
    # check if forth bit from the right is one 
    mask = 0b1000
    
    if (mask & input) > 0: # 1 
        return "on" 
    else:
        return "off"

    


# Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.

a = 0b10111011

mask = 0b100 #third bitfrom the right turn on 

print bin(a | mask) 



# flip all the bits in "a"

a = 0b11101110

mask = 0b11111111

print bin(a ^ mask)





# slide operators into place using left and right shifts 

def flip_bit(number, n):
    
    mask = (0b1 << n - 1 )
    result = number ^ mask
    
    return bin(result) 



