#include <stdio.h>

int main()
{
    int i, start, end, sum = 0;

    printf("Input the upper limit: ");
    scanf("%d", &end);
    printf("Input the lower limit: ");
    scanf("%d", &start);

    for (i = start; i <= end; i++)
    {
        sum += i;
    }
    printf("The sum from %d to %d is %d", start, end, sum);
    printf("\n");
    return 0;
}