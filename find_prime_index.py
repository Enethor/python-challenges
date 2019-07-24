# What is the 10 001st prime number?


def find_prime_by_index(index):
    primes = [1, 2]
    x = 3
    while len(primes) <= index:
        for i in range(2, x):
            if x % i == 0:
                x += 1
                break
            elif x % i != 0 and i == x - 1:
                primes.append(x)
                x += 1
    print(primes[index])


find_prime_by_index(10001)
