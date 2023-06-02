#include <stdio.h>

// food, leisure, clothes, accommodation and travel
int main()
{
    float foodExpenses;
    printf("\n Enter food expenses: ");
    scanf(" %f", &foodExpenses);

    float leisureExpenses;
    printf("\n Enter leisure expenses: ");
    scanf(" %f", &leisureExpenses);

    float clothesExpenses;
    printf("\n Enter clothes expenses: ");
    scanf("%f", &clothesExpenses);

    float accomodationExpenses;
    printf("\n Enter accomodation expenses: ");
    scanf("%f", &accomodationExpenses);

    float travelExpenses;
    printf("\n Enter travel expenses: ");
    scanf("%f", &travelExpenses);

    float total;
    total = foodExpenses + leisureExpenses + clothesExpenses + accomodationExpenses + travelExpenses;

    printf("You spent");
    printf("\nFood: £%.2f", foodExpenses);
    printf("\nLeisure: £%.2f", leisureExpenses);
    printf("\nClothes: £%.2f", clothesExpenses);
    printf("\nAccomodation: £%.2f", accomodationExpenses);
    printf("\nTravel: £%.2f", travelExpenses);
    printf("\nTotal spent: £%.2f",total);
    printf("\n\n");
    return 0;
}