#include <bits/stdc++.h>
#include <string>
using namespace std;



int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
    string list[10] = {"zero","one","two","three","four","five","six","seven","eight","nine" } ;
    if ( n > 9) {
        cout << "Greater than 9" << endl ;

    }
    else {
        cout << list[n] << endl ;
    }




    return 0;
}
