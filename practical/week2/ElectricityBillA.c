#include <stdio.h>
int main()
{
    //define variables for previous and current readings
    int day, month, previous, next;

    //prompt user to enter previous and current readings, day and month //separated by a space or return;
    printf("Input the previous the day, month, the previous and next \n");
    scanf("%d %d %d %d", &previous, &next, &day, &month);

    //read previous metre, current metre, day and month //display previous metre, current metre, day and month //Validation
    //current metre reading within range 0..9999 //sample code below
    if (9999 > next > 0 && 9999 > previous > 0)
    {
        if (previous > next)
        {
            printf("The previous reading cannot be bigger than the next one");
        }
        else if ((next - previous) > 1000)
        {
            printf("You could not have used that much energy");
        }
        else
        {

            switch (month)
            {
            case 2:
            {
                if (0 > day || day > 29)
                {
                    printf("The day is wrong");
                }
                else
                {
                    printf("All good!");
                }
            }
            break;

            case 1:;
            case 3:;
            case 5:;
            case 7:;
            case 8:;
            case 11:;
            case 12:
            {
                if (0 > day || day > 31)
                {
                    printf("The day is wrong");
                }
                else
                {
                    printf("All done!");
                }
            };
            break;
            case 4:;
            case 6:;
            case 9:;
            case 10:
                if (0 > day || day > 30)
                {
                    printf("The day is wrong");
                }
                else
                {
                    printf("All done!");
                }break;
            default:
                printf("The month is wrong");
                break;
            }
        }
    }
    else
    {
        printf("The values are out of range");
    }

    return 0;
}