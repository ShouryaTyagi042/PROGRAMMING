#include <stdio.h>
long int power() ;
int main() {
    printf("exponential is %ld",power(7));

}

long int power(int x) {

    long int p ;
    p = 3 ;
    if (x== 1) {
        return p ;
    }

    else {

        p = 3 * power(x-1) ;
        // x++ ;

    }
    return p ;
}
