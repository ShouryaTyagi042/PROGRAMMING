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
    int n, x, c;
    cin >> n >> x >> c;
    int arr[n];
    int sum = 0;
    FOR(i, n)
    {
        cin >> arr[i];
        sum += arr[i];
    }
    sort(arr, arr + n);
    if (arr[0] >= x)
    {
        cout << sum << "\n";
        return;
    }
    int temp = sum;
    int current = sum;

    FOR(i, n)
    {
        current = sum + (x - arr[i]) - c * (i + 1);
        sum = sum + (x - arr[i]);
        // cout << temp << " ";
        if (temp <= current)
        {
            temp = current;
        }
        else
        {
            break;
        }
    }
    // cout << "\n";
    cout << temp << "\n";
    return;
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