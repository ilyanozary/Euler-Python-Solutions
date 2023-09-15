def prime_factors(number):
    factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return factors


number = 600851475143
factors = prime_factors(number)

print(f"Prime factors {number}:")
for factor in factors:
    print(factor)
