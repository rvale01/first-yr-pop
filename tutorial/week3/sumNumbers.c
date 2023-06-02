#include <stdio.h>

int main()
{
    int i, n, sum = 0;

    printf("Input the upper limit: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        sum += i;
    }
    printf("Sum of the first %d numbers is %d", n, sum);
    printf("\n");
    return 0;
}