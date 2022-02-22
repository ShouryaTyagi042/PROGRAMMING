#include <stdio.h>
#include <stdbool.h>

int main() {
    bool flag = true ;
    int sum = 0 ;
    while(flag==true) {
        int n ;
        scanf("%d",&n) ;
        sum += n ;
        if (n==0) {
            flag = false ;
        }

    }
    printf("Your sum is %d ",sum);

}

/*
wap sum of two matrices
wap to find sum and product of all elements of 2d array


*/
