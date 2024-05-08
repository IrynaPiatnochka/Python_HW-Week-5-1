# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}
# Capitilization matters

def solution (str):
    astring = {}
    for i in str:
        if i in astring:
            astring[i] += 1
        else:
            astring[i] = 1
    return astring
        
