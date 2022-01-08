#include <bits/stdc++.h>
#include <cstdio>
// #include <conio.h>
using namespace std ;
void sum_of_digits(int num)  {
    int sum = 0 ;
    while (num != 0) {
        sum += num % 10 ;
        // cout << sum << endl ;
        num = num / 10 ;
    }
    cout << sum << endl ;

}

int main() {
    int test_cases ;
    cin >> test_cases ;
    for (int i = 0; i < test_cases; ++i)
    {
        int number ;
        cin >> number ;
        sum_of_digits(number) ;

    }
    return 0 ;

}
