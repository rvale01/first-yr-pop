#include <stdio.h>

// struct 

int smallBig(int *a)
{
    for (int x = 0; x < 1; x++)
    {
        if (a[x] > a[x + 1])
        {
            int temp = a[x];
            a[x] = a[x + 1];
            a[x + 1] = temp;
        }
    }
    return 0;
}

int main()
{
    int *a;

    for (int x = 0; x < 2; x++)
    {
        printf("Input integer %d ", x+1);
        scanf("%d", &a[x]);
    }

    smallBig(a);
    printf("Smallest : %d", a[0]);
    printf("Largest : %d", a[1]);
    return 0;
}