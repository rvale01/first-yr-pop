#include <stdio.h>

int main()
{
    int arr[3][4];
    int column[4]={0,0,0,0};
    printf("Enter a 3 by 4 matrix: ");
    for (int x = 0; x < 3; x++)
    {
        for (int y = 0; y < 4; y++)
        {
            scanf("%d", &arr[x][y]);
            column[y] = column[y] + arr[x][y];
        }
    }
    for (int i = 0; i < 4; i++)
    {
       printf("%d \n", column[i]);
    }

    return 0;
}