class PrimeFactors:

    @staticmethod
    def generate(number):
        primes = []

        for possible_prime in range(2, number+1):
            if number % possible_prime == 0:
                primes.append(possible_prime)

                while number % possible_prime == 0:
                    number = number / possible_prime

                if number == 1:
                    break

        return primes
