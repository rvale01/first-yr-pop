#include <stdio.h>
#include <stdbool.h>

int main()
{
    int size = 10;
    int sizeR = 3;
    int sizeC = 10;
    float criminal[sizeR][sizeC];
    float suspect[size];
    int x;
    printf("Enter the 10 chromosomes of the suspect separated by spaces: \n");
    for (x = 0; x < size; x++)
    {
        scanf(" %f", &suspect[x]);
    }

    for (x = 0; x < sizeR; x++)
    {
        printf("Enter the 10 chromosomes of the %dth criminal: \n", x + 1);
        for (int j = 0; j < sizeC; j++)
            scanf(" %f", &criminal[x][j]);
    }

    // match the DNA
    bool match;
    int criminalMatch;
    for (x = 0; x < sizeR; x++)
    {
        match = true;
        for (int j = 0; j < sizeC; j++)
            if (suspect[j] != criminal[x][j])
            {
                match = false;
            }
            
        if (match)
        {
            criminalMatch = x;
            break;
        }
        
    }

    // printf("%d", criminalMatch + 1);

    // display
    if (match)
        printf("The DNA of the suspect is a match with criminal n.%d", criminalMatch + 1);
    else
        printf("The DNA pf the suspect does not match with any of the criminals");
    printf("\n");
    return 0;
}