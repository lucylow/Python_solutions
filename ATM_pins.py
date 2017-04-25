# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

def validate_pin(pin): # pin is a string 

    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit() == False: # use str.isdigit() method 
            return False 
        return True

    return False
        

    
