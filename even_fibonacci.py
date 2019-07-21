# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

top_range = 4000000

def fibonacci(max_range):
    acumulator = 2
    last_number = 1
    even_valued_sum = 0

    while acumulator <= max_range:
        if acumulator % 2 == 0:
            even_valued_sum += acumulator
            print(even_valued_sum)
        
        last_number_holder = acumulator
        acumulator += last_number
        last_number = last_number_holder

fibonacci(top_range)
    
