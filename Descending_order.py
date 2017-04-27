def Descending_Order(num):

    num = str(num) 
    num = list(num)
    num = sorted(num)
    num = "".join(num)
    num = num[::-1]
    return int(num)
