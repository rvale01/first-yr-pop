#include <stdio.h>

int main()
{
    float celsiusValue;
    float fahrenheitValue;
    printf("Enter a degree in Celsius: ");
    scanf("%f", &celsiusValue);
    fahrenheitValue = celsiusValue * (9.0 / 5.0) + 32.0;

    printf("%f", celsiusValue );
    printf("\n%.2f",fahrenheitValue);
    printf("\n\n");
    return 0;
}