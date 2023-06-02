#include <stdio.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

int main()
{
    int employeesHours[8][7];
    int totalHours[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    for (int x = 0; x < 8; x++)
    {
        printf("\nEmployee %d", x);
        for (int y = 0; y < 7; y++)
        {
            scanf("%d", &employeesHours[x][y]);
            totalHours[x] += employeesHours[x][y];
        }
    }

    // display in decreasing order with bubble sort
    int i, j;
    for (i = 0; i < 7; i++)

        // Last i elements are already in place
        for (j = 0; j < 8 - i - 1; j++)
            if (totalHours[j] > totalHours[j + 1])
                swap(&totalHours[j], &totalHours[j + 1]);

    for (int x = 0; x < 8; x++)
    {
        printf("\n%d", totalHours[x]);
    }
    return 0;
}