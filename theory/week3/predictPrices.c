#include <stdio.h>

int main()
{
    double price = 200000;
    int years = 0;
    while (price < 400000)
    {
        price *= 1.05;
        years++;
    }
    printf("After %d years the cost of a house is %.2f", years, price);
    return 0;
}