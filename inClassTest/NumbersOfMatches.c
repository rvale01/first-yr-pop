#include <stdio.h>
/*
@author Valentina Ronchi
@date 24/10/2020
@student n 20035819
@group CP2/05
@description: This program will find and display the number of preferences each of the students shares with the user
without telling him/her the order of these preferences.
The values are taken from a file
*/
FILE *fp;

int main()
{
    fp = fopen("preferences.txt", "r");

    // declare variables used in the project
    int nOfFriends = 5;                    //number of friends
    int listOfMovies = 5;                  //number of movies choosen by each person
    int student[listOfMovies];             //represents the list of top 5 preferences from the given student
    int friends[nOfFriends][listOfMovies]; //represents the five lists of top 5 preferences from the five friends
    int sharedPref;                        //the number of preferences each person shares with the user //value used in the loop

    // fill the student array with values from the file
    for (int x = 0; x < listOfMovies; x++)
    {
        fscanf(fp, "%d", &student[x]);
    }

    // fill the friends array with values from the file
    for (int x = 0; x < nOfFriends; x++)
    {
        for (int y = 0; y < listOfMovies; y++)
        {
            fscanf(fp, "%d", &friends[x][y]);
        }
    }

    // find and display the number of preferences each of the friends shares with the user
    for (int x = 0; x < nOfFriends; x++) //loop trough the friend
    {
        sharedPref = 0;
        for (int y = 0; y < listOfMovies; y++) //loop trough the list of each friend
        {
            for (int z = 0; z < listOfMovies; z++) //loop trough the list of the student
            {
                if (friends[x][y] == student[z]) //check if values match
                {
                    sharedPref++; //if values match add 1 to sharedPref
                    break;
                }
            }
        }

        //print the results for each friend
        printf("Friend %d shares %d preferences\n", x, sharedPref);
    }

    return 0;
}
