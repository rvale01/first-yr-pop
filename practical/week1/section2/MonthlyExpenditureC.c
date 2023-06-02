
#include <stdio.h>

int main()
{
    float foodExpenses = 150.0;
    float leisureExpenses = 40.0;
    float clothesExpenses = 100.5;
    float accomodationExpenses = 200.0;
    float travelExpenses = 300.0;

    float total;
    total = foodExpenses + leisureExpenses + clothesExpenses + accomodationExpenses + travelExpenses;

    printf("The total spent this month is £%.1f", total);
    return 0;
}