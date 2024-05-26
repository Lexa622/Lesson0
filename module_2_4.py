numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for j in numbers:
        if j != i and i % j == 0 and j != 1:
            not_primes.append(i)
            is_prime = True
            break
        elif i != 1:
            is_prime = False
    if is_prime == 0:
        primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
