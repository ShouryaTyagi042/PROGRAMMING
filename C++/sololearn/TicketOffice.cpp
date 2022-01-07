#include <bits/stdc++.h>
using namespace std;

int main() {
    int ages[5];

    for (int i = 0; i < 5; ++i) {
        cin >> ages[i];
        // cout << ages[i] << endl ;
    }
    int min_age = ages[0] ;
    for (int j = 0 ; j<5 ; j++) {
        if (min_age > ages[j]) {
            min_age = ages[j] ;

        }
    }
    float ticket , discount ;
    discount = (min_age) * 0.5 ;
    ticket = 50.0 - discount ;
    cout << ticket ;






    return 0 ;
}



