#include <stdio.h>
FILE *fp;

int main()
{
    fp = fopen("dna_input.txt", "r");
    double arr[10];
    double total;
    for (int x = 0; x < 10; x++)
    {
        fscanf(fp, "%lf", &arr[x]);
        total += arr[x];
    }

    printf("The total is : %.2lf", total);
    fclose(fp);
}