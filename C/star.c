#include <stdio.h>

int main() {
    int n = 5 ;
    for (int i = 1 ; i <= n ; i++) {
        // printf("*")
        for( int j = n - i ; j > 0 ; j--) {
            printf(" ") ;
        }
        for ( int j = 0 ; j < i   ; j++ ) {
            printf("%c",65+j);
        }
        for (int j = i - 1 ; j > 0 ; j--){
            printf("%c",64+j) ;
        }
        printf("\n") ;
    }
}


// inverted pyramid
