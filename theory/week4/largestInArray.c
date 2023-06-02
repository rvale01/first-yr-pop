#include <stdio.h>
FILE *fp;

int main()
{
    fp = fopen("dna_input.txt", "r");
    double arr[10];
    double largest;
    for (int x = 0; x < 10; x++)
    {
        fscanf(fp, "%lf", &arr[x]);
        if(x == 0 || largest<arr[x]){
            largest = arr[x];
        }
    }
    printf("%.1lf", largest);
    fclose(fp);
}