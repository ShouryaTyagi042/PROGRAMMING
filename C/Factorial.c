// WAP to find the factorial of number given through keyboard.
// WAP to print all the numbers between 10 and 20.
// WAP to print out the sum of first n natural numbers using while loop.

#include <stdio.h>

int main() {
    int n ;
    int fact = 1 ;
    scanf("%d",&n) ;
    if ( n == 1) {
        // printf()
        printf("Your factorial is %d",fact) ;
        return 0 ;
    }
    for ( int i = 1 ; i < n+1 ; i++) {
        fact = fact * i ;
    }
    printf("Your factorial is %d ",fact) ;
    return 0 ;
}
