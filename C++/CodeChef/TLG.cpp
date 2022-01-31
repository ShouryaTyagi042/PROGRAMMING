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

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout) ;
    #endif
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T;
    cin >> T;
    int f = T ;
    // int diff[T] ;
    int p1sum = 0 ;
    int p2sum = 0 ;
    int p1arr[T] , p2arr[T] ;
    int i = 0 ;
    while (T > 0 ) {
        int p1 , p2 , d ;
        cin >> p1 >> p2 ;
        // cout << p1 << " " << p2 << "\n" ;
        p1sum += p1 ;
        p2sum += p2 ;
        d = p1sum - p2sum ;
        if ( d > 0) {
            p1arr[i] = d ;
            p2arr[i] = 0 ;
        }
        else {
            d = d * -1 ;
            p2arr[i]  = d ;
            p1arr[i] = 0 ;
        }
        i++ ;
        T-- ;
    }
    
    int max1 = 0 ; 
    int max2 = 0 ;

    FOR (a,f) {
        if ( max1 < p1arr[a] ) {
            max1 = p1arr[a] ;
        }
        if ( max2 < p2arr[a] ) {
            max2 = p2arr[a] ;
        }
    } 
    if ( max1 > max2) {
        cout << 1 << " " << max1 << "\n" ;
    }
    else{
        cout << 2 << " " << max2 << "\n" ;
    } 


    return 0;
}