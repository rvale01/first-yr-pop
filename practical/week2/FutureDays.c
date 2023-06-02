#include <stdio.h>

int main()
{
    char list[7][30]={
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    };
    int day, elapsedDay;
    printf("Enter today's day: \n");
    scanf("%d", &day);

    printf("Enter the number of days elapsed since today: \n");
    scanf("%d", &elapsedDay);

    elapsedDay = elapsedDay%7;

    printf("Today is %s", list[day]);
    printf(" and the future day is %s", list[elapsedDay+day]);

}