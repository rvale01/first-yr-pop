#include <stdio.h>

int main()
{
    int row, columns, maxRow, maxTotal;
    printf("Input the row: ");
    scanf("%d", &row);

    printf("Input the column: ");
    scanf("%d", &columns);

    printf("Intpu the matrix: ");
    int arr[row][columns];
    for (int i = 0; i < row; i++)
    {
        int total = 0;
        for (int x = 0; x < columns; x++)
        {
            scanf("%d", &arr[i][x]);
            total += arr[i][x];
        }
        if (total > maxTotal)
        {
            maxTotal = total;
            maxRow = i;
        }
    }

    printf("The row with the max total is : %d", maxRow + 1);

    return 0;
}