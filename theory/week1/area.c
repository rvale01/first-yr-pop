#include <stdio.h>

int main(){
    //declare variables for radius and area
    float radius;
    float area;

    const float PI = 3.14159;

    //prompt the user to enter a radiu
    printf("Input the radius ");
    scanf("%f", &radius);

    //asign a value to radius
    radius = 20;
    //Compute the area given a radius and assign the result to area
    area = radius * radius * PI;

    //Display result
    printf("\nThe area of the circle of radius %.2f", radius);
    printf("is %.2f", area);

    return 0;
}
