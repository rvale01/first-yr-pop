#include <stdio.h>
double largerSalary(double salary1, double salary2);
double smallerSalary(double salary1, double salary2);
int main()
{
    double salary1, salary2, mortgage;

    printf("Input the salary one: \n");
    scanf("%lf", &salary1);

    printf("Input the salary two: \n");
    scanf("%lf", &salary2);

    mortgage = largerSalary(salary1, salary2) * 3 + smallerSalary(salary1, salary2);

    printf("The maximum size of the morgage is : %.2f", mortgage);
    return 0;
}

double largerSalary(double salary1, double salary2)
{
    if (salary1 > salary2)
    {
        return 1;
    }

    return salary2;
}

double smallerSalary(double salary1, double salary2)
{
    if (salary1 > salary2)
    {
        return 1;
    }

    return salary2;
}