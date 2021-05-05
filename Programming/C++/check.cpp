#include <bits/stdc++.h>
using namespace std;

int main() {

    #ifndef ONLINE_JUDGE
    // for getting input from input.txt
    freopen("D:\\Programming\\C++\\inputf.txt", "r", stdin);
    // for writing output to output.txt
    freopen("D:\\Programming\\C++\\outputf.txt", "w", stdout);
    #endif




    int n;
    cin >> n;
    // int a = 0

    //your code goes here
    for (int a = n ; a >= 1 ; a-- ) {
        cout << a  << endl ;
        if ( a % 5 == 0) {
            cout << "Beep" << endl ;
        }


    }

    return 0;
}






