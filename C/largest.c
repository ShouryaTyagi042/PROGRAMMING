#include <stdio.h>

int main() {
    int n1 , n2 , n3 ;
    // cin >> n1 >> n2 >> n3 ;
    scanf("%d %d %d",&n1,&n2,&n3);
    int max = n1 ;
    if ( n1 < n2 ) {
        max = n2 ;
    }
    if ( n3 > max) {
        max = n3 ;
    }
    printf("%d \n",max) ;
}
