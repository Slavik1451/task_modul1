numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = [], []
for num in range(1, len(numbers)):
    is_prime = True
    for j in range(2, numbers[num]):
        if numbers[num] % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(numbers[num])
    else:
        not_primes.append(numbers[num])
print(f'Primes:{primes}\nNot_primes:{not_primes}')
