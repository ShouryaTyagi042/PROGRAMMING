#include <bits/stdc++.h>
#include <cstdio>
using namespace std ;

int main() {
    int ques,ans ;
    cin >> ques ;
    ans = 0 ;
    for (int i = 0 ; i < ques ; i++ ) {
        int a,b,c ;
        scanf("%d %d %d",&a,&b,&c) ;
        if (a+b+c >= 2) {
            ans++ ;
        }
    }
    cout << ans ;


    return 0 ;


}












