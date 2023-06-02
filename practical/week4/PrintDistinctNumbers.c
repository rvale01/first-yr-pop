#include <stdio.h>
#include <stdbool.h>

int main()
{
    int array1[10], distinct[10];
    int numb;
    bool search;
    printf("Enter 10 numbers");
    for (int x = 0; x < 10; x++)
    {
        scanf("%d", &array1[x]);
    }

    distinct[0] = array1[0];
    for (int x = 0; x < 10; x++)
    {
        search = true;
        if (x != 0)
        {
            for (int y = 0; y < x; y++)
            {
                if (array1[x] == distinct[y])
                    search = false;
            }
        }
        if(search){
            distinct[x] = array1[x];
            numb++;
        }
    }

    printf("%d", numb);
    return 0;
}