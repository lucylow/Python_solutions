def is_prime(x):
    if x <= 1:
        return False
    else:
        for i in range(2, x-1): # 2,3,4,5,6.. etc
            if x % i == 0:
                return False
        return True
