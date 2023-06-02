#include <stdio.h>

int displaySortedNumbers(double num1, double num2, double num3)
{
    printf("Test");
    double arr[3] = {num1, num2, num3};
    for (int i = 0; i < 3 - 1; i++)

        // Last i elements are already in place
        for (int j = 0; j < 3 - i - 1; j++)
            if (arr[j] > arr[j + 1])
            {
                double temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }

    printf("Sorted numbers: ");
    for (int x = 0; x < 3; x++)
    {
        printf("%.1lf\n", arr[x]);
    }
    return 0;
}

int main()
{
    double arr[3];
    for (int x = 0; x < 3; x++)
    {
        printf("Input value n. %d ", x + 1);
        scanf("%lf", &arr[x]);
    }
    printf("Test");
    displaySortedNumbers(arr[0], arr[1], arr[2]);
    return 0;
}