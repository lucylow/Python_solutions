def factorial(x):
    
    if x == 1:
        return 1 # factorial of 1 is 1 
        
    else:
        ans = x
        
        while x > 1:
            
            ans *=  x-1 
            
            x -= 1 # decrement, avoid infinite loop 
            
        return ans 
