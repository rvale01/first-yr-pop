#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main()
{
    char arr[30];
    int digits;
    printf("Input a password: \n");
    scanf(" %s", arr);
    //     fgets(pass, sizeof(pass), stdin);

    if (arr[7] == '\0')
    {
        printf("Too short!");
    }
    else
    {
        int size;
        for (int x = 0; arr[x] != '\0'; x++)
        {
            if (isdigit(arr[x]))
            {
                digits++;
            }
            else if (!isalpha(arr[x]))
            {
                printf("Invalid Password\n");
            }
            size++;
        }

        printf("%d", digits);
        if(digits<2){
            printf("Invalid Password\n");
        }else{
            printf("Valid Password");
        }

    }

    return 0;
}