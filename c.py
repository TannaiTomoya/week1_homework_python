primes = []

for number in range(2, 41):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(number)
print(primes)
