#include <stdio.h>
FILE *fp;

int main()
{
    fp = fopen("inputFile.txt", "r");

    char firstWord[20];
    char secondWord[20];
    int num;

    int x;

    for (x = 0; x < 3; x++)
    {
        fscanf(fp, "%s %s %d", firstWord, secondWord, &num);
        printf("%s %s \n%d \n", firstWord, secondWord, num);
        printf("\n");
    }
}