#include <bits/stdc++.h>
using namespace std ;

int main() {
    float num ;
    cin >> num ;
    int a = num ;
    cout << a << endl;
    float frac = num - a ;
    cout << frac << endl ;
    int int_frac = frac * 1000000 ;
    int_frac ++ ;
    cout << int_frac << endl ;
    int sum = 0 , d ;
    // double constant = 10 ;

    while (int_frac > 0) {
        d = int_frac % 10 ;
        sum += d ;
        int_frac = int_frac / 10 ;
    }
    cout << sum << endl;

    return 0;
}
