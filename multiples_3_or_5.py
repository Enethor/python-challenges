# The sum of all the numbers which are multiples of 3 or 5 below 1000

max_number = 1000

def check_multiples(max) :
    acumulator = 0
    for x in range(1, max):
        if x % 3 == 0 or x % 5 == 0:
            acumulator += x
    print(acumulator)

check_multiples(max_number)
    
    
