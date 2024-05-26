numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[j] != numbers[i] and numbers[i] % numbers[j] == 0 and numbers[j] != 1:
            not_primes.append(numbers[i])
            is_prime = True
            break
        elif numbers[i] != 1:
            is_prime = False
    if is_prime == 0:
        primes.append(numbers[i])
print('Primes:', primes)
print('Not Primes:', not_primes)
