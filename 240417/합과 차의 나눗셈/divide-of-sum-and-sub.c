#include <stdio.h>

int main() {
    int a, b ;
    double c;
    scanf("%d %d", &a, &b);
    printf("%.2lf", (double)(a+b)/(a-b));
    return 0;
}