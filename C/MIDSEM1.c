#include <stdio.h>
int main() {
    int arr[3][3] ;
    for( int i = 0 ; i < 3 ; i++) {
        for ( int j = 0 ; j < 3  ; j++) {
            int n ;
            scanf("%d ",&n) ;
            arr[i][j] = n ;

        }
    }
    for( int i = 0 ; i < 3 ; i++) {
        for ( int j = 0 ; j < 3  ; j++) {
            int flag = 0 ;
            // for ( int k = 1 ;  )
            for ( int k = 2 ; k <= arr[i][j]/2 ; k++) {
                if ( arr[i][j] % k == 0) {
                    flag = 1 ;
                }

            }
            if ( flag == 0]) {
                printf("%d",arr[i][j]) ;
            }

        }}

}
