###Implement a function which filters out array values which satisfy the given predicate.

###reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]


def reject(seq, predicate): 
    
    actual_result = []    
    bool_result = [predicate(value) for value in seq]
    i = 0
    
    for value in bool_result:
        if value == False:
            actual_result = actual_result + [seq[i]]
        i = i+1
    return actual_result 
