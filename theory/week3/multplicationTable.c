#include <stdio.h>

int main()
{
    int x, y;
    printf("    Multiplication table \n");
    for(x = 1; x<10; x++){
        printf("  %d", x);
    }
    printf("\n-----------------------------\n");

    for (x = 1; x < 10; x++)
    {
        printf("%d |", x);
        for(y = 1; y<10;y++){
            printf("%d ", y*x);
        }
        printf("\n");
    }
    return 0;
}