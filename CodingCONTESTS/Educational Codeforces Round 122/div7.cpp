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
    int n ;
    cin >> n ;
    if ( n % 7 == 0) {
        cout << n << "\n" ;
        return ;
    }
    int n1 , n2 ;
    n1 = n - n % 7 ;
    int q = n / 7 + 1 ;
    n2 = 7 * q ;
    if ( n % 10 >= n % 7  ) {
        cout << n1 << "\n" ;
        return ;
    }
    cout << n2 << "\n" ;
    return ;

}
int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout) ;
    #endif
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T;
    cin >> T;
    while (T > 0 ) {
        solve();

        T -- ;

    }
    return 0;
}