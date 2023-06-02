#include <stdio.h>

 powMethod(x, n)
{
    if (n == 0) return 1;

    if(n%2==0) return powMethod(x*x, n /2);
    else return x * powMethod(x, n - 1);   
    return 0;
}

long powmod2(x, n, m)
{
    long y = powMethod(x, n);
    return y%m;
}

long powmod1(x, n, m){
    long z = x;
    for(int y = 0; y<n-1; y++){
        z %= x;
    }
    return z%m;
}
int main()
{
    long result = powmod2(29, 100000000, 773);
    printf("%lu \n", result);
    result = powmod1(29, 100000000, 773);
    printf("%lu", result);
    return 0;
}