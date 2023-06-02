#include <stdio.h>
FILE *fp;
int main()
{
    fp = fopen("dna_input.txt", "r");

    double arr[10];
    
    printf("Reading from file");

    for (int x = 0; x < 10; x++)
    {
        fscanf(fp, "%lf", &arr[x]);
    }

    printf("\nPrinting values on the console: ");

    for(int x = 0; x<10; x++){
        printf(" %.1lf ", arr[x]);
    }
    fclose(fp);
}