# Display prime numbers
# Compare with PrimeNumber.c from Week 3

NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10

count = 0  # start counting from zero
number = 2  # set next number to be tested to 2

print("The first 50 prime number are:")
while count < NUMBER_OF_PRIMES:
    isPrime = True
    divisor = 2
    while divisor <= number/2:
        if number % divisor == 0:
            isPrime = False
        divisor += 1
    if isPrime:
        count += 1
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to new line
            print(number)
        else:
            # Display the number, don't advance
            print(number, end=" ")
    number += 1
