#include <stdio.h>

int main()
{
    int i, n, sum = 0;

    printf("Input the upper limit: ");
    scanf("%d", &n);

    for (i = 2; i <= n; i+=2)
    {
        sum += i;
    }
    printf("Sum of the first %d numbers is %d", n, sum);
    printf("\n");
    return 0;
}