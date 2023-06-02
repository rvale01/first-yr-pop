#include <stdio.h>

int main()
{
    int value = 0;
    int max = 0;
    int occurrence= 0;
    printf("Input the integers. The last digit has to be 0\n");

    do
    {
        printf("Input:");
        scanf("%d", &value);
        if(max<value){
            max = value;
            occurrence = 1;
        }else if (max == value){
            occurrence++;
        }
    } while (value != 0);

    printf("%d %d", max, occurrence);
    return 0;
}