#include <stdio.h>
// food, leisure, clothes, accommodation and travel
int main()
{
    const int ACCOMODATION = 300;
    float foodExpenses;
    float leisureExpenses;
    float clothesExpenses;
    float travelExpenses;

    printf("\n Enter food expenses: ");
    scanf(" %f", &foodExpenses);

    printf("\n Enter leisure expenses: ");
    scanf(" %f", &leisureExpenses);

    printf("\n Enter clothes expenses: ");
    scanf("%f", &clothesExpenses);

    printf("\n Enter travel expenses: ");
    scanf("%f", &travelExpenses);

    float total;
    total = foodExpenses + leisureExpenses + clothesExpenses + ACCOMODATION + travelExpenses;

    printf("You spent");
    printf("\nFood: £%.2f", foodExpenses);
    printf("\nLeisure: £%.2f", leisureExpenses);
    printf("\nClothes: £%.2f", clothesExpenses);
    printf("\nAccomodation: £%d", ACCOMODATION);
    printf("\nTravel: £%.2f", travelExpenses);
    printf("\nTotal spent: £%.2f", total);
    printf("\n\n");

    return 0;
}