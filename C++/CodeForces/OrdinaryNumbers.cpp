#include <bits/stdc++.h>
#include <string>
using namespace std ;

// void solve() {
//     int n,res ;
//     cin >> n ;
//     res = 0 ;
//     for (int i = 0 ; i<= n ; i++) {
//         res += i  ;

//     }
//     cout<< res << endl ;


// }
// int main()
// {
//     int t ;
//     cin >> t ;
//     while (t-- > 0) {
//         solve() ;
//     }
//     return 0;
// }


void solve() {
    int n , res ;
    cin >> n ;
    res = 0 ;
    if (n > 9) {
        for ( int i = 1 ;i <=n ; i++) {
            int x ;
            string str1 ;
            str1 = to_string(i) ;
            x = str1.length() ;
            for (int j = 1 ; j < x ; j++){
                if (str1[0] != str1[j]){

                    break ;


                }
                else {
                    res ++ ;
                }
            }




        }
      cout << res + 9 << endl ;
      }
    else {
        res = n ;
        cout << res << endl ;
    }




}
int main() {
    int t ;
    cin >> t ;
    while (t-- > 0 ) {
        solve() ;

    }
    return 0 ;

}
