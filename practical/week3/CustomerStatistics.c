#include <stdio.h>
FILE *fp;

int main()
{
    fp = fopen("testInput.txt", "r");

    // variables needed in the program
    int lines, customerID, previousReading, currentReading, x, totalReading, totalHeavy, totalRegular, totalLight;
    printf("reading from file: \n");
    fscanf(fp, "%d", &lines);
    for (x = 0; x < lines; x++)
    {
        printf("Reading again...\n");
        fscanf(fp, "%d %d %d", &customerID, &previousReading, &currentReading);
        totalReading = currentReading - previousReading;
        printf("%d", customerID);
        if (totalReading > 1000)
        {
            ++totalHeavy;
        }
        else if (totalReading < 500)
        {
            ++totalLight;
        }
        else
        {
            ++totalRegular;
        }
    }

    printf("\n");
    printf("Heavy users %d", totalHeavy);
    printf("\nRegular users %d", totalRegular);
    printf("\nLight users %d", totalLight);
    return 0;
}