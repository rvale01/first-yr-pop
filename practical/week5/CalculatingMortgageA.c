#include <stdio.h>

int main()
{
    double salary1, salary2, largerSalary, smallerSalary, mortgage;

    printf("Input the salary one: \n");
    scanf("%lf", &salary1);

    printf("Input the salary two: \n");
    scanf("%lf", &salary2);

    if (salary1 > salary2)
    {
        largerSalary = salary1;
        smallerSalary = salary2;
    }
    else
    {
        largerSalary = salary2;
        smallerSalary = salary1;
    }

    mortgage = largerSalary * 3 + smallerSalary;

    printf("The maximum size of the morgage is : %.2f", mortgage);

    return 0;
}