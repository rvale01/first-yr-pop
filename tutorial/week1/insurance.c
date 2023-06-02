#include <stdio.h>

int main()
{
    printf("Hello\n");
    int age;

    printf("Enter your age: \n");
    scanf("%d", &age);

    if (age > 65)
    {
        printf("You can't enter the site as you are too old");
    }
    else if (age < 18)
    {
        printf("You can't enter the site as you are too young");
    }
    else if (age >= 18 || age <= 65)
    {
        printf("You can enter the site");
    }
    else
    {
        printf("The age entered is wrong!");
    }

    return 0;
}