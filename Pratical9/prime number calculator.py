def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


number_to_test = 29
print(f"Is {number_to_test} a prime number? {is_prime(number_to_test)}")
