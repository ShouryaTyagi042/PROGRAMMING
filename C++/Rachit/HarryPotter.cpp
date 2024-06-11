#include <iostream>
#include <map>
#include <array>
using namespace std;
#define max(a, b) (a < b ? b : a)
#define min(a, b) ((a > b) ? b : a)
// #define mod 1e9 + 7`
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

int binarySearch(int arr[], int l, int r, int x)
{
    while (l <= r)
    {
        int m = l + (r - l) / 2;
        if (arr[m] == x)
            return m;
        if (arr[m] < x)
            l = m + 1;
        else
            r = m - 1;
    }
    return -1;
}

void solve()
{
    int m, n;
    cin >> m >> n;
    int arr[m][n];
    int sorted_array[m * n];
    int sorted_array_indices[m][n];
    FOR(i, m)
    {
        FOR(j, n)
        {
            cin >> arr[i][j];
            sorted_array[i * n + j] = arr[i][j];
        }
    }
    for (int i = 0; i < m * n; i++)
    {
        for (int j = 0; j < m * n - i - 1; j++)
        {
            if (sorted_array[j] > sorted_array[j + 1])
            {
                int temp = sorted_array[j];
                sorted_array[j] = sorted_array[j + 1];
                sorted_array[j + 1] = temp;
            }
        }
    }
    FOR(i, m)
    {
        FOR(j, n)
        {
            int index = binarySearch(sorted_array, 0, m * n - 1, arr[i][j]);
            sorted_array_indices[i][j] = index + 1;
        }
    }
    int sum = 0;
    FOR(i, m)
    {
        for (int j = i; j < n; j++)
        {
            int x = sorted_array_indices[i][j];
            int y = sorted_array_indices[i][n - j - 1];
            sum += max(x, y) - min(x, y);
        }
    }
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
