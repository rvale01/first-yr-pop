/* Print monthly expenditure Practical 1, Part 2 (a) @author your name */
#include <stdio.h>

int main()
{
    float foodExpenses = 300.0;
    float leisureExpenses = 100.0;
    float clothesExpenses = 250.5;
    float totalExpenses;
    totalExpenses = foodExpenses + leisureExpenses + clothesExpenses;
    printf("The total expenditure this month was £%.2f\n\n", totalExpenses);
    return 0;
}