#include <stdio.h>

int main() {
    int n ;
    printf("Enter the value of n in nxn");
    scanf("%d",&n) ;
    int arr1[n][n] ;
    int sum = 0 ;
    int product = 1 ;
    for (int i = 0 ; i < n ; i++) {
        for (int j = 0 ; j< n ; j++) {
            // int x ;
            printf("Enter element [%d,%d] : ",i+1,j+1);
            scanf("%d",&arr1[i][j]) ;
            sum += arr1[i][j] ;
            product *= arr1[i][j] ;

        }
        // printf("\n") ;
    }
    printf("Sum is %d \n",sum);
    printf("product is %d ",product);


}
