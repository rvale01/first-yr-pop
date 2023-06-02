#include <stdio.h>

struct Obj
{
    int a;
    char c[30];
};

struct Obj getValues(struct Obj object1)
{
    printf("In the function: ");
    printf("%s ", object1.c);
    printf("%d\n\n", object1.a);
    return object1;
}

int main()
{
    struct Obj object2;
    printf("Input an integer : ");
    scanf("%d", &object2.a);

    printf("Input a char or a string: ");
    scanf("%s", object2.c);

    printf("Before the function: ");
    printf("%s ", object2.c);
    printf("%d\n", object2.a);
    printf("\n\n");
    
    object2 = getValues(object2);
    printf("After the function: ");
    printf("%s ", object2.c);
    printf("%d\n", object2.a);
    return 0;
}