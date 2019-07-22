# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def find_smallest_multiple(cap):
    smallest_multiple = cap
    state = True
    while state:
        for x in range(1, cap+1):
            if smallest_multiple % x == 0 and x != cap:
                continue
            elif smallest_multiple % x == 0 and x == cap:
                print(smallest_multiple)
                state = False
                break
            else:
                break
        smallest_multiple += 1


find_smallest_multiple(20)
