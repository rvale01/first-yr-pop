#include <stdio.h>

int main()
{
    const char list[12][20] = {
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"};
    int month, year, day;
    printf("Input the month and year: ");
    scanf("%d %d", &month, &year);

    switch (month)
    {
    case 2:
    {
        if (year % 400 == 0 || day % 4 == 0)
        {
            day = 29;
        }
        else
        {
            day = 28;
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
        day = 31;
    };
    break;
    case 4:;
    case 6:;
    case 9:;
    case 10:
        day = 30;
        break;
    default:
        printf("The month is wrong");
        break;
    }

    printf("In the month of %s", list[month-1]);
    printf(" in the year %d", year);
    printf(" there are %d", day);
    printf("days");

    return 0;
}