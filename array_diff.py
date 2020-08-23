
# "Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b."



def array_diff(a, b):
    for i in b:
        if i in a:
            for j in range(a.count(i)): ## for the number of times 'i' of 'b' appears in 'a'
                a.remove(i)             ### loop to remove 'i' from 'a'
    return a
