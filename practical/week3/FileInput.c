/* read values from input file Practical 3, Part 2
@author your name */

#include <stdio.h>
FILE *fp;

int main()
{
    // open the file and assign its address/disk location to file pointer
    fp = fopen("inputFile.txt", "r"); //relative pathname used

    // declare variables for holding the values of input
    char firstWord[20]; // a word/string up to 20 characters
    char secondWord[20];
    int num;
    //remind user - program reads to input values
    printf("Reads two words and an integer from file \n");
    // read two words and an integer from file
    fscanf(fp, "%s %s %d", firstWord, secondWord, &num);
    // display two words and an integer
    printf("Displays back what has been read from input file:\n");
    printf("%s %s \n%d \n", firstWord, secondWord, num);

    fclose(fp); // always close files you've opened
}