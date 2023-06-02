#include <stdio.h>

int main()
{
    int rows, columns;
    printf("Enter the rows: ");
    scanf("%d", &rows);
    printf("Enter the columns: ");
    scanf("%d", &columns);

    int arr[rows][columns];

    printf("Enter %d rows with %d colums each ", rows, columns);
    for (int i = 0; i < rows; i++)
    {
        for (int x = 0; x < columns; x++)
        {
            scanf("%d", &arr[i][x]);
        }
    }

     for (int i = 0; i < rows; i++)
    {
        for (int x = 0; x < columns; x++)
        {
            printf("%d ", arr[i][x]);
        }
        printf("\n");
    }
    
    return 0;
}