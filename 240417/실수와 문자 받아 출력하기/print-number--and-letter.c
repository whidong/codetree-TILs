#include <stdio.h>

int main() {
    char a;
    double b, c;
    scanf("%c %lf %lf", &a, &b, &c);
    printf("%c\n%.2lf\n%.2lf", a, b, c);
    return 0;
}