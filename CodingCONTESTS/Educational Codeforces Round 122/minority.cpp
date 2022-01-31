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
void solve () {
    string s ;
    cin >> s ;
    map<string,int> m ;
    int n = s.length() ;
    // cout << n ;
    // return ;

    for(int i = 0 ; i < n ; i++ ) {
        if (s[i]=='1') {
            m["1"]++ ; 
        }
        else{m["0"]++;} ;
    }
    // cout << m["0"] << " " << m["1"] << "\n" ;
    if (m["1"] == m["0"] ) {
        cout << m["1"] - 1 << "\n" ;
        return ;
    }
    cout << min(m["1"],m["0"]) << "\n" ;
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