#include <bits/stdc++.h>
using namespace std ;

void printArray(int a[],int n){
    for(int i=0;i<n;i++)
      cout<<a[i]<<" ";
    cout<<endl;
}
int main() {
    int n ;
    cin>> n ;
    int arr[n] ;
    for ( int i = 0 ; i <n ; i++) {
        cin >> i ;
        arr[i] = i ;
    }
    printArray(arr,n);

    return 0 ;
}
