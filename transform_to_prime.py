import math

def minimum_number(numbers):
    first_sum = sum(numbers)
    next_sum = first_sum
    
    while is_prime(next_sum)!=True:
        next_sum += 1
    else:
        not_sum = (next_sum) - (first_sum)
        return (not_sum)
        
        
def is_prime(n):
    if n == 2 or n == 3 or n == 7:
        return True
    if n % 2 == 0 or n <= 1 or n % 3 == 0:
        return False
        
    sqr = int(math.sqrt(n)) + 1
    
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
