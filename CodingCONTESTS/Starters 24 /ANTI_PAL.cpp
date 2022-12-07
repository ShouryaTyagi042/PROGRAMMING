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
    string s ;
    cin >> s ;
    if ( n % 2 != 0) {
        cout << "NO" << "\n" ;
        return ;
    } 
    sort(s.begin(),s.end()) ;
    int max_f = 1 ;
    int temp = 1 ;
    for ( int i = 0 ; i < n -1  ; i++) {
        if ( s[i] == s[i+1]) {
            temp ++  ;
        }
        else {
            max_f = max(max_f,temp) ;
            temp = 1 ;
        }
    }
    if ( max_f > n/2) {
        cout << "NO" << '\n' ;
        return ;
    }
    reverse(s.begin(),s.begin()+n/2);
    string ans = "" ;
    for (char ch: s) {
        ans += ch ;
    }
    cout << "YES" << '\n' ;
    cout << ans << '\n';
    return ;

    
    
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
    while (T > 0 ) {
        solve();

        T -- ;

    }
    return 0;
}