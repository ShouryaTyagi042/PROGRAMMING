#include <stdio.h>

int main() {
    int n ;
    scanf("%d",&n) ;
    int sum = 0 ;
    while ( n > 0) {
        sum += n ;
        n -- ;
    }
    printf("Sum of N natural numbers is %d ",sum);
}
