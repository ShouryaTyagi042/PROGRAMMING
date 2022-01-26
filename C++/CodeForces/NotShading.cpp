#include <bits/stdc++.h>
using namespace std;
#define max(a, b) (a < b ? b : a)
#define min(a, b) ((a > b) ? b : a)
// #define mod 1e9 + 7
#define FOR(a, c) for (int(a) = 0; (a) < (c); (a)++)
// #define FORL(a, b, c) for (int(a) = (b); (a) <= (c); (a)++)
// #define FORR(a, b, c) for (int(a) = (b); (a) >= (c); (a)--)
#define INF 1000000000000000003
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
#define F first
#define S second
#define PB push_back
#define POB pop_back
#define MP make_pair
void solve() {
    int row , column , cellr , cellc ;
    cin >> row >> column >> cellr >> cellc ;
    // vector<vector<char> > mat ;
    bool flag = true ;
    bool flag2 = true ;
    bool flag3 = true ;
    FOR (i,row) {
        // mat.PB(vector<char> row) ;
        FOR( j , column) {
            char c ;
            cin >> c ;
            if ( i + 1 == cellr && j + 1 == cellc ){
                if (c == 'B') {
                    cout << 0 << endl ;
                    flag = false ;
                    
                }
            }
            if ( i +1 == cellr || j+1 == cellc  ) {
                if (c== 'B') {
                    flag2 = false ;
                }
            
            }
            if ( c == 'B')   {
                flag3 = false ; 

            }                
    }  
    }
    if (flag2 == false && flag3 == false) {
        if (flag != false) {
            cout << 1 << endl ;
        }
        
    }
    if ( flag3 == false && flag2 == true ){
        cout << 2 << endl ;
    }
    if ( flag2 == true && flag3 == true) {
        cout << -1 << endl;
    }

}


    
    


int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout) ;
    #endif
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T;
    cin >> T;
    while (T > 0) {
        int ans ;
        solve();
     
        T-- ;

    }
    return 0;
}
