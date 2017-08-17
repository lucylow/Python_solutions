'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

'''


def sort_array(A):
    odds = []
    
    for i, item in enumerate(A):
        if item % 2 == 1: odds.append(item)
    
    odds.sort()
    i_odd = 0

    for j, item in enumerate(A):
        if item % 2 == 1:
            A[j] = odds[i_odd]
            i_odd += 1
    return A
