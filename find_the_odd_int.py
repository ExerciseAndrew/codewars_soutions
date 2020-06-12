#Given an array, find the integer that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

def find_it(arr): 
    size = len(arr)        
    Hash=dict() 
    
    for i in range(size): 
        
        Hash[arr[i]]=Hash.get(arr[i],0) + 1 
    for i in Hash: 
  
        if(Hash[i]% 2 != 0): 
            return i 

    return -1
    
    #I need to write test cases for everything.
