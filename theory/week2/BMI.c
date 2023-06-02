#include <stdio.h>
#define CONVERSION_TO_KG 0.453599237;
#define CONVERSION_TO_CM 0.0254;

int main()
{
    float weight, height, bmi;
    printf("Input your weight in pounds: ");
    scanf("%f", &weight);
    weight = weight * CONVERSION_TO_KG;

    printf("Input your height in inches: ");
    scanf("%f", &height);
    height = height * CONVERSION_TO_CM;

    bmi = weight / pow(height, 2);

    if (bmi < 18.5)
    {
        printf("Underweight");
    }
    else if (25.0 > bmi >= 18.5)
    {
        printf("Normal");
    }
    else if (30.0 > bmi >= 25.0)
    {
        printf("Overweight");
    }
    else if (bmi >= 30.0)
    {
        printf("Obese");
    }

    return 0;
}