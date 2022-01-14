#include <bits/stdc++.h>
using namespace std;

int main() {
    string a,b ;
    cin >> a >> b ;
    cout << a.size() <<" " << b.size() << endl ;
    cout << a+b << endl ;
    char d ;
    d = a[0] ;
    a[0] = b[0] ;
    b[0] = d ;
    cout << a << " " << b ;


  
    return 0;
}
