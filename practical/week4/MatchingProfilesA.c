#include <stdio.h>
#include <stdbool.h>

int main()
{
    int size = 10;
    float criminal[size], suspect[size];
    int x;
    printf("Enter the 10 chromosomes of the suspect separated by spaces: \n");
    for (x = 0; x < size; x++)
    {
        scanf(" %f", &suspect[x]);
    }

    printf("Enter the 10 chromosomes of the criminal separated by spaces: \n");
    for (x = 0; x < size; x++)
    {
        scanf(" %f", &criminal[x]);
    }

    // match the DNA
    bool match = true;
    for (x = 0; x < size; x++)
    {
        if (criminal[x] != suspect[x])
            match = false;
    }

    // display
    if (match)
        printf("The two DNAs are a match");
    else
        printf("The two DNAs are not a match");
    printf("\n");
    return 0;
}