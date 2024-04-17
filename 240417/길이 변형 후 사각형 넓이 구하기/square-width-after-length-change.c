#include <stdio.h>

int main() {
	int a ,b;
    scanf("%d %d", &a, &b);
    a = a+8;
    b = b*3;
	printf("%d \n%d \n%d", a , b, a * b);
    return 0;
}