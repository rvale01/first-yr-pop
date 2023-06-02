#include <stdio.h>
/*
@author Valentina Ronchi
@group CP2/05
*/

// main function
int main()
{
    //variables used to store the quantity of pizzas
    int smallQuantity, mediumQuantity, largeQuantity;

    // variable used to store the total spent
    double totalSpent;

    // prompt the user to input the quantity of small pizzas and save the value
    printf("Enter the number of small pizzas:\n");
    scanf("%d", &smallQuantity);
    printf("\n");

    // prompt the user to input the quantity of medium pizzas and save the value
    printf("Enter the number of medium pizzas:\n");
    scanf("%d", &mediumQuantity);
    printf("\n");

    // prompt the user to input the quantity of large pizzas and save the value
    printf("Enter the number of large pizzas:\n");
    scanf("%d", &largeQuantity);
    printf("\n");

    // fixed cost of a large, a medium, a small pizza saved as double constant
    const double LARGECOST = 10.60;
    const double MEDIUMCOST = 8.20;
    const double SMALLCOST = 5.80;

    // calculating the total cost of all pizzas (total of the order)
    totalSpent = smallQuantity * SMALLCOST + mediumQuantity * MEDIUMCOST + largeQuantity * LARGECOST;

    // output of the total spent by the user
    printf("The total cost of your order is £%.1lf", totalSpent);
    printf("\n");
    return (0);
}
