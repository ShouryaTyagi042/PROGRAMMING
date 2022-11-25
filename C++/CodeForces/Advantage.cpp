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
    FOR(i, l)
    {
        cin >> arr[i];
    }
    int first = 0, second = -1;
    for (int i = 1; i < l; i++)
    {
        if (arr[i] > arr[first])
        {
            second = first;
            first = i;
        }
        else if (arr[i] < arr[first])
        {
            if (second == -1 || arr[second] < arr[i])
                second = i;
        }
    }
    int max = arr[first], s_max = arr[second];
    FOR(i, l)
    {
        if (arr[i] == max)
        {
            if (max == s_max)
            {
                cout << 0 << " ";
            }
            else
            {
                cout << max - s_max << " ";
            }
        }
        else
        {
            cout << arr[i] - max << " ";
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