#include <stdio.h>

int main()
{
    float annualInterestRate, numberOfYears, loanAmount;
    // Prompt the user to enert the annual interest rate, the number of years, and the loan amount
    printf("Enter annual interest rate ");
    scanf("%f", &annualInterestRate);

    printf("Enter number of years as integer");
    scanf("%f", &numberOfYears);

    printf("Enter the loan amount");
    scanf("%f", &loanAmount);

    // Compute the monthly interest rate
    float monthlyInterestRate = annualInterestRate / 1200;
    // Compute the payments
    float monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / pow(1 + monthlyInterestRate, numberOfYears * 12));
    float totalPayment = monthlyPayment * numberOfYears * 12;

    // Display the payments
    printf("The monthly payment is £%.2f \n", monthlyPayment);
    printf("The total payment is £%.2f \n", totalPayment);
    return 0;
}
