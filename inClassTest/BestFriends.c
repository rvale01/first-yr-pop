/* 
Full Name: Valentina Ronchi
Date: 1/12/2020
Group: CP2/05
Student n.: 20035819
Description: This program will ask two users to input their preferencies. The program then checks if at least 3 of the 5 top preferencies
match in the exact same position.
*/


#include <stdio.h>
#include <stdbool.h>

// function where the two arrays are checked
bool matchPreferencies(int friendA[], int friendB[])
{
    int preferencies = 0; //variable used to count how many preferencies match
    for (int x = 0; x < 5; x++)
    {
        if (friendA[x] == friendB[x])
        {
            preferencies++; //increase the value if two preferencies match at exact position
        }
    }

    if (preferencies >= 3) //check if the preferencies are equal or more than 3
        return true;       //if yes return true

    return false; //in any other case, the function will return false
}


// main function
int main()
{
    int friendA[5];
    int friendB[5];

    // ask friend A his/her preferencies
    printf("Friend A\n");
    for (int y = 0; y < 5; y++)
    {
        scanf("%i", &friendA[y]);
    }

    // ask friend B his/her preferencies
    printf("Friend B\n");
    for (int y = 0; y < 5; y++)
    {
        scanf("%i", &friendB[y]);
    }

    //pass the arrays to the function and store the return of the function
    bool match = matchPreferencies(friendA, friendB);

    // check the return of the function
    if (match)
        printf("Good match!"); //if true
    else
        printf("Not good match"); //if false

    return 0;
}