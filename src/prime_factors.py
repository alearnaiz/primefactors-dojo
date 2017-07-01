class PrimeFactors:

    @staticmethod
    def generate(number):
        primes = []

        for possible in range(2, number+1):
            if possible > number:
                break

            if number % possible == 0:
                primes.append(possible)
                while number % possible == 0:
                    number = number / possible

        return primes
