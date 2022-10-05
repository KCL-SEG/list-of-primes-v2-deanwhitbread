"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    try:
        list = []

        if number_of_primes < 1:
            raise ValueError(f'Cannot compute {number_of_primes} prime numbers!')
        else:
            number = 2

            while number_of_primes:
                if isPrime(number):
                    list.append(number)
                    number_of_primes = number_of_primes - 1
                number = number + 1

        return list
    except ValueError as ve:
        print(ve)
        raise
    except Exception as e:
        print("The value you have given is wrong; only integars greater than zero are allowed!")
        raise

    return list

def isPrime(number):
    if number == 2:
        return True
    elif number == 3:
        return True
    else:
        for value in range(2, number):
            if (number % value) == 0:
                return False
        else:
            return True
    return False
