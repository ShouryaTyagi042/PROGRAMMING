#include <bits/stdc++.h>
using namespace std ;
int search ( int arr[], int size , int num) {
    int c =  -1 ;
    for(int i = 0 ; i < size ; i++) {
        if ( num == arr[i]) {
            c = i ;
        }
    }
    return c ;
}

int main() {
    int arr[3] = {1,2,3} ;
    int n = 3 ;
    int x = sizeof(arr) / sizeof(arr[0]) ;
        int result = search(arr , x , n) ;
        cout << result << "\n" ;



    return 0 ;
}
