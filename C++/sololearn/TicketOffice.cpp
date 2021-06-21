#include <bits/stdc++.h>
using namespace std;

int main() {
    int ages[5];

    for (int i = 0; i < 5; ++i) {
        cin >> ages[i];
    }
    //your code goes here
    float min ;
    min = ages[0] ;
    for (int i = 0; i < 5; i++ ){

        if (min > ages[i]) {
            min = ages[i] ;
        }

    }
    cout << min << endl ;
    double ans ;
    ans = 50.0 * (100.0-min) / 100.0 ;
    cout << ans ;




    return 0;
}
