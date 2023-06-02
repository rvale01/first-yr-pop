#include <stdio.h>
// Read a sequence of values from keyboard into an array

int main()
{
    double arr[10];
    printf("Input 10 values: ");
    for (int x = 0; x < 10; x++)
    {
        scanf("%lf", &arr[x]);
    }

    return 0;
}