#include <stdio.h>
/*
@author Valentina Ronchi
@group CP2/05
*/

// main function
int main()
{
    // declare id and miles
    int walkerId, miles;

    // prompt the user to input id and miles
    printf("Please input walker identification number and miles walked: ");
    scanf("%d %d", &walkerId, &miles);

    printf("\n");

    // validate the id
    if (walkerId > 99)
        printf("Error: club ID is Invalid (too high)\n"); //if the id is too high there is an error
    else if (walkerId < 1)
        printf("Error: club ID is Invalid (too low)\n"); //if the id is too low there is an error

    // validate the miles
    else if (miles > 30)
        printf("Error: the miles are Invalid (too high)\n"); //if the id is fine but the miles are too high there is an error
    else if (miles < 5)
        printf("Error: the miles are Invalid (too low)\n"); //if the id is fine but the miles are too low there is an error

    // if both id and miles are fine the user is classified in one of the three groups 
    // and the result is displayed on the console
    else if (miles >= 21 && miles <= 30)
        printf("The user %d is a serius walker", walkerId);
    else if (miles >= 11 && miles <= 20)
        printf("The user %d is a regular walker", walkerId);
    else
        printf("The user %d is a leisure walker", walkerId);

    printf("\n");
    return 0;
}