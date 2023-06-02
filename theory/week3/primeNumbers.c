#include <stdio.h>
#include <stdbool.h>

int main()
{
    const int NUMBER_OF_PRIMES = 50;
    const int NUMBER_OF_LINES = 10;
    int count = 0;
    int number = 2;

    printf("The first 50 prime numbers are:\n");

    while (count < 50)
    {
        bool isPrime = true;
        for (int divisor = 2; divisor <= number / 2; divisor++)
        {
            if (number % divisor == 0)
            {
                isPrime = false;
                // break;
            }
        }
        if (isPrime)
        {
            count++; // Increase count
            //display it
            if (count % NUMBER_OF_LINES == 0)
            {
                // Display the number and advance to the new line
                printf("%d \n", number);
            }
            else
                printf("%d ", number); //display it
        }

        // Increment next number by 1
        number++;
    }
    return 0;
}