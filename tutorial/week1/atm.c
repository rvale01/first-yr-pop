#include <stdio.h>

int main()
{
    int option;
    int balance = 100;
    int withdraw;
    int deposit;

    printf("\nWelcome! Choose one of the options: ");
    printf("\n1. Display your bank balance\n");
    printf("2. Withdraw money\n");
    printf("3. Update your balance\n");
    scanf("%d", &option);

    switch (option)
    {
    case 1:
    {
        printf("Your balance is: %d", balance);
        printf("\n");
    }
    break;
    case 2:
    {
        printf("Input the amount of money you want to withdraw: ");
        scanf("%d", &withdraw);
        if (withdraw > balance)
        {
            printf("You don't have enough money in your account!");
        }
        else
        {
            balance -= withdraw;
            printf("Your new balance is: %d", balance);
        }
        printf("\n");
    }
    break;
    case 3:
    {
        printf("Input the amount of money you want to deposit: ");
        scanf("%d", &deposit);
        balance += deposit;
        printf("Your new balance is: %d", balance);
        printf("\n");
    }
    default:
        printf("The choice is wrong!\n");
        break;
    }

    return 0;
}