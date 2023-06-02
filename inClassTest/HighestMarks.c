#include <stdio.h>
/*
@author Valentina Ronchi
@date 17/10/2020
@student n 20035819
@group CP2/05
@description: This program reads values in a file and check for the highest mark among all the marks of a class
*/
//file pointer
FILE *fp;

// main function
int main()
{
    // opening the file
    fp = fopen("marks.txt", "r");

    // varibales used // tempMark is a temporary variable used to hold the mark from the file and to compare it with the highest mark
    int nOfStudents, moduleCode, highestMark, tempMark;
    // reading first the module code and the the number of student and save them in variables
    fscanf(fp, "%d %d", &moduleCode, &nOfStudents);

    // loop through the marks
    for (int x = 0; x < nOfStudents; x++)
    {
        // get the marks from the file
        fscanf(fp, "%d", &tempMark);
        // check if the mark of each student is in the range
        if (tempMark > 100 || tempMark < 0)
        {
            // if it is not in range, stop the loop and save the highestMark as -1
            highestMark = -1;
            break;
        }

        //if it's in range and the the temp value is higher than the highestMark
        // or if it's the first value of the loop, the value of highestMark will change
        else if (x == 0 || tempMark > highestMark)
            highestMark = tempMark;
    }

    // if the highestMark is -1, there was something wrong with one or more marks, so an error is displayed
    if (highestMark == -1)
    {
        printf("%d invalid marks \n", moduleCode);
    }
    else //if the highest is not equal to 0, there was no error
    {

        printf("%d %d \n", moduleCode, highestMark);
    }

    fclose(fp);
}