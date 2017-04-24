#Isograms

# An isogram is a word with no repeating letters, consecutive or non-consecutive.

def is_isogram(string):
    if len(string) ==0:
        return True
    elif sorted(set(string.upper())) == sorted(string.upper()):
        return True
    else:
        return False

