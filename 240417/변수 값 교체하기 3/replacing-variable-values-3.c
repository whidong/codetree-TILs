#include <stdio.h>

int main() {
    int a = 3;
    int b = 5;
    int temp;
    temp = a;
    a = b;
    b = temp;
    printf("%d\n%d", a , b);
    return 0;
}