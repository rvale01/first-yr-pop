#include <stdio.h>
#include <stdbool.h>
FILE *fp;

int main()
{
    fp = fopen("dna_input.txt", "r");
    int size = 10;
    int numbOfCriminals;
    float suspect[size];

    for (int x = 0; x < size; x++)
    {
        fscanf(fp, "%f", &suspect[x]);
    }

    fscanf(fp, "%d", &numbOfCriminals);

    float criminals[numbOfCriminals][size];
    for (int x = 0; x < numbOfCriminals; x++)
    {
        for (int y = 0; y < size; y++)
        {
            fscanf(fp, "%f", &criminals[x][y]);
        }
    }

    // match the DNA
    bool match;
    int criminalMatch;
    for (int x = 0; x < numbOfCriminals; x++)
    {
        match = true;
        for (int j = 0; j < size; j++)
            if (criminals[x][j] != suspect[j])
            {
                match = false;
            }

        if (match)
        {
            criminalMatch = x;
            break;
        }
    }

    // display
    if (match)
        printf("The DNA of the suspect is a match with criminal %d", criminalMatch + 1);
    else
        printf("The DNA pf the suspect does not match with any of the criminals");
    printf("\n");
    fclose(fp);
}