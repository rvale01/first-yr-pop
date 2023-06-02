#include <stdio.h>

int main()
{
    const int currentPop = 312032486;
    const int oneYear = 31536000;
    const int birth = 7;
    const int death = 13;
    const int immigrants = 45;

    int totBirth = oneYear / birth;
    int totDeath = oneYear / death;
    int totImm = oneYear / immigrants;

    int totPopulation1 = currentPop + totBirth - totDeath + totImm;
    int totPopulation2 = totPopulation1 + totBirth - totDeath + totImm;
    int totPopulation3 = totPopulation2 + totBirth - totDeath + totImm;
    int totPopulation4 = totPopulation3 + totBirth - totDeath + totImm;
    int totPopulation5 = totPopulation4 + totBirth - totDeath + totImm;
    printf("\nPopulation after one year: %d", totPopulation1);
    printf("\nPopulation after two years: %d", totPopulation2);
    printf("\nPopulation after three years: %d", totPopulation3);
    printf("\nPopulation after four years: %d", totPopulation4);
    printf("\nPopulation after five years: %d", totPopulation5);
    printf("\n\n");
    return 0;
}