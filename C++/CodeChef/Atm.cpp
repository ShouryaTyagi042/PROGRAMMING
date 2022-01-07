#include <bits/stdc++.h>
#include <iostream>
using namespace std ;

int main() {
    int withdraw ;
    float balance ;
    // float current = balance - withdrawn - 0.50 ;
    // cout << current ;
    cin >> withdraw >> balance ;
    float debit = withdraw + 0.50 ;
    if (debit <= balance && withdraw % 5 == 0) {
        float new_balance = balance - debit ;
        printf("%.2f",new_balance) ;
    }
    else {
        printf("%.2f",balance) ;
    }

    return 0 ;


}

