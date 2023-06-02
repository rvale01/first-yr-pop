#include <stdio.h>

int main()
{
    int age = 10;
    double girl[3], boy[3];
    int boyCount = 0;
    int girlCount = 0;
    int same = 0;
    for (int x = 0; x < 3; x++)
    {
        int y = x + 10;
        printf("The twins are : %d \n", y);
        printf("Input the height of the girl: ");
        scanf("%lf", &girl[x]);
        printf("Input the height of the boy: ");
        scanf("%lf", &boy[x]);

        if (girl[x] > boy[x])
            girlCount++;
        else if (girl[x] < boy[x])
            boyCount++;
        else
            same++;
    }

    printf("The girl is taller than the boy: %d times\n", girlCount);
    printf("The boy is taller than the girl: %d times\n", boyCount);
    printf("They are the same height: %d times\n", boyCount);
    return 0;
}