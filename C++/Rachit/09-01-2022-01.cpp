# include <bits/stdc++.h>
using namespace std ;

int main() {
    int n ;
    cin >> n ;
    for (int i =1 ; i<=n ;i++ ) {
        for (int j =1 ; j<= n-i; j++) {
            cout << " " ;
        }
        int l1 = i / 10 ;
        // cout << l1 ;
        int l2 = i % 10 ;
        // cout << l2 ;
        int t = 1 ;
        while (t<=l1) {
            for (int j = 1 ; j<=9 ; j++) {
                cout << j ;
            }
            cout << 0 ;
            t++ ;
        }
        for (int j = 1 ; j <= l2 ; j++) {
            cout << j ;
        }

        for (int j = l2-1 ; j > 0 ; j--) {
            cout << j ;
        }
        int t2 = 1 ;
        while (t2<=l1) {
            cout << 0 ;
            for (int j = 9 ; j>0 ; j--) {
                cout << j ;
            }
            t2++ ;
        }


        cout << endl ;

    }
}
