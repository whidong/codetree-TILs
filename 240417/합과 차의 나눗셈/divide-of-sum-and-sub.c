#include <stdio.h>

int main() {
    int a, b ;
    double c;
    scanf("%d %d", &a, &b);
    c = a+b;
    c = c/(a-b);
    printf("%.2lf", c);
    return 0;
}