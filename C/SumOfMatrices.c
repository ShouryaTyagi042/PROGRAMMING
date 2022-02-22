#include <stdio.h>

int main() {
    int n ;
    printf("Enter the value of n in nxn");
    scanf("%d",&n) ;
    int arr1[n][n] ;
    int arr2[n][n] ;
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j< n ; j++) {
            // int x ;
            printf("Enter element [%d,%d] : ",i+1,j+1);
            scanf("%d",&arr1[i][j]) ;

        }
        // printf("\n") ;
    }
    printf("Second Array\n");
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j< n ; j++) {
            // int x ;
            printf("Enter element [%d,%d] : ",i+1,j+1);
            scanf("%d",&arr2[i][j]) ;

        }
        // printf("\n") ;
    }
    int sum[n][n] ;
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j< n ; j++) {
            sum[i][j] = arr1[i][j] +arr2[i][j];
        }
        // printf("\n") ;
    }
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j< n ; j++) {
            printf("%d ",sum[i][j]) ;

        }
        printf("\n") ;
    }
    return 0;

}
