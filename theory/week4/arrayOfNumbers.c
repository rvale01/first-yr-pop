#include <stdio.h>

int main()
{
    int size, elements;
    double average, total;

    printf("Enter the number of items: ");
    scanf("%d", &size);
    double arr[size];
    printf("\nEnter the numbers: ");
    for (int x = 0; x < size; x++)
    {
        scanf("%lf", &arr[x]);
        total += arr[x];
    }

    average = total / size;
    for (int x = 0; x < size; x++)
    {
        if (arr[x] > average)
        elements++;
    }

    printf("The average is: %.2lf \n", average);
    printf("There are %d elements above average", elements);
    return 0;
}