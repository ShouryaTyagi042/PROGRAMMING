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
void solve()
{
    int l;
    cin >> l;
    int arr[l];
    int copy[l];
    FOR(i, l)
    {
        cin >> arr[i];
    }
    FOR(i, l)
    {
        copy[i] = arr[i];
    }
    sort(copy, copy + l);
    FOR(i, l)
    {
        if (arr[i] == copy[l - 1])
        {
            cout << arr[i] - copy[l - 2] << " ";
        }
        else
        {
            cout << arr[i] - copy[l - 1] << " ";
        }
    }
    cout << "\n";
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T;
    cin >> T;
    while (T > 0)
    {
        solve();

        T--;
    }
    return 0;
}