#include <bits/stdc++.h>
#include <string>
using namespace std ;


int main() {
    int x ;
    cin >> x ;
    for (int i = 0 ; i <= x ; i++) {
        string str ;
        getline(cin,str) ;
        int a = str.length() ;
        if (a>10) {
            cout << (str[0]+to_string(a-2)+str[a-1]) << endl ;

        }
        else {
            cout << str << endl ;
        }


    }







    return 0 ;
}
