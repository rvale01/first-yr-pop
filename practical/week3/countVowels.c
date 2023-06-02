#include <stdio.h>

int main()
{
    char inputString[50];
    printf("Enter a string: ");
    fgets(inputString, sizeof(inputString), stdin);

    int x;
    int numberVowels = 0;
    int numberConsonant = 0;

    for (x = 0; inputString[x] != '\0'; x++)
    {
        if (inputString[x] == 'a' || inputString[x] == 'e' || inputString[x] == 'i' || inputString[x] == 'o' || inputString[x] == 'u')
            numberVowels++;

        else if (inputString[x] != ' '  && inputString[x] >= 'a' && inputString[x] <= 'z')
            numberConsonant++;
    }

    printf("The number of vowels is: %d", numberVowels);
    printf("\nThe number of consonants is: %d", numberConsonant);
    printf("\n");
    return 0;
}