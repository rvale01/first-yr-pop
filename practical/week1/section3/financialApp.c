#include <stdio.h>

int main()
{
    float monthlySavings;
    float yearInterestRate;
    float monthInterestRate;
    float totalValue;
    printf("How much are you saving each month?");
    scanf("%f", &monthlySavings);

    printf("What is the yearly interest rate?");
    scanf("%f", &yearInterestRate);

    monthInterestRate = yearInterestRate / 1200;

    int i;
    for (i = 0; i < 6; i++)
    {
        totalValue = (totalValue + monthlySavings) * (1.0 + monthInterestRate);
    }

    printf("The total after six months %.2f", totalValue);

    return 0;
}