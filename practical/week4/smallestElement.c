#include <stdio.h>

int main()
{
    // declare an array of double
    double arr[10];
    // declare a double to store the smallest value
    double smallest;
    printf("Input the 10 values: ");
    for (int x = 0; x < 10; x++)
    {
        scanf("%lf", &arr[x]);
        // check for the smallest value
        if (smallest > arr[x] || x==0)
        {
            smallest = arr[x];
        }
    }

    printf("The smallest value in the list is: %.1lf ", smallest);

    return 0;
}