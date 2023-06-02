#include <stdio.h>
#include <stdbool.h>
bool isPrimeCheck(int number)
{
    for (int divisor = 2; divisor <= number / 2; divisor++)
    {
        if (number % divisor == 0)
        {
            return false;
        }
    }
    return true;
}
int main()
{
    const int NUMBER_OF_PRIMES = 50;
    const int NUMBER_OF_LINES = 10;
    //set count (number of primes) to 0
    int count = 0;
    //set number (next number to be tested) to 2
    int number = 2;
    //Repeatedly find and display prime numbers
    //until 50 primes found
    while (count < 50)
    {
        bool isPrime = isPrimeCheck(number);

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
}