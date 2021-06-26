#include <bits/stdc++.h>
using namespace std ;

void printArray(int a[],int n){
    for(int i=0;i<n;i++)
      cout<<a[i]<<" ";
    cout<<endl;
}

void solve() {
    int n ;
    cin >> n ;
    int arr[n] ;
    for (int i = 1 ; i <= n ; i++) {
        arr[i-1] = i ;
    }
    for (int g = 0 ;g<n-1 ;g = g+2 ) {
            int k ;
            k = arr[g];
            arr[g] = arr[g+1] ;
            arr[g+1] = k ;
    }
    if ( n %2 != 0) {
        int l ;
        l = arr[n-2] ;
        arr[n-2] = arr[n-1] ;
        arr[n-1] = l ;
    }


    printArray(arr,n) ;
}
int  main() {
    int t ;
    cin >> t ;
    // cout << t << endl ;
    while (t-- > 0) {
        solve() ;
    }
    return 0 ;
}
