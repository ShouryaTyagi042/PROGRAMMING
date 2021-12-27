// #include <bits/stdc++.h>
// using namespace std;

// int main() {

//     int n;
//     cin >> n;
//     // int a = 0

//     //your code goes here
//     for (int a = n ; a >= 1 ; a-- ) {
//         cout << a  << endl ;
//         if ( a % 5 == 0) {
//             cout << "Beep" << endl ;
//         }


//     }

//     return 0;
// }
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a = n ;
    while (a<=1) {
        cout << a << endl ;
        if (a%5 == 0) {
            cout << "Beep" << endl ;
        }
        a-- ;

    }



    return 0;
}






