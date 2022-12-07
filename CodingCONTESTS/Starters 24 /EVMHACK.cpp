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
    int arr[6] ;
    int sum = 0 ;
    int max = 0 ;
    int index ;
    for(int i = 0 ; i < 6 ; i++) {
        cin >> arr[i] ;
        if( i > 2) {
            sum += arr[i] ;
            if ( max < arr[i] - arr[i-3]) {
                max = arr[i] - arr[i-3] ;
                index = i ;
            }
        }

    }
    int votes = 0 ;
    for ( int i = 0 ; i < 3 ; i++) {
        if ( i == index - 3 ) {
            votes += arr[index] ;
        }
        else {
            votes += arr[i] ;
        }
    }
    if (votes > sum / 2.0) {
        cout << "YES" << "\n" ;
        return ;
    }
    cout << "NO" <<"\n" ;
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