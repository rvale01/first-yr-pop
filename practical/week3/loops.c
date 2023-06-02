#include <stdio.h>

int main()
{
    int x, y;
    for (x = 0; x < 7; x++)
    {
        for (y = 1; y <= x; y++)
        {
            printf("%d", y);
        }
        printf("\n");
    }
    printf("\n\n");

    for (x = 7; x > 0; x--)
    {
        for (y = 1; y < x; y++)
        {
            printf("%d", y);
        }
        printf("\n");
    }

    for (x = 1; x < 7; x++)
    {
        for (y = 6; y > 0; y--)
        {
            if (y <= x)
            {
                printf("%d", y);
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }
    printf("\n\n");

    for (x = 0; x < 6; x++)
    {

        for (y = 1; y < 7; y++)
        {
            if ((y - x) > 0)
            {
                printf("%d", y - x);
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}