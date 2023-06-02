#include <stdio.h>
FILE *fp;
int main()
{
    fp = fopen("students.txt", "r");
    char votes[8][10];
    char ans[10];
    int count;

    for (int x = 0; x < 10; x++)
    {
        fscanf(fp, " %s", &ans[x]);
    }

    for (int x = 0; x < 8; x++)
    {
        for (int y = 0; y < 10; y++)
        {
            fscanf(fp, " %s", &votes[x][y]);
        }
    }

    for (int i = 0; i < 8; i++)
    {
        count = 0;
        for (int x = 0; x < 10; x++)
        {
            if (votes[i][x] == ans[x])
                count++;
        }
        printf("\nStudent n. %d has %d right votes", i + 1, count);
    }
    fclose(fp);
}