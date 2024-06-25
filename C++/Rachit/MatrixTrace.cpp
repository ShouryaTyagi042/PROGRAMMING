#include <iostream>
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
    int n;
    cin >> n;
    // create the matrix from the input
    int S[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> S[i][j];
        }
    }
    int maxTrace = INT_MIN;
    // Iterate over all possible sizes of the submatrix
    for (int k = 1; k <= n; k++)
    {
        // Iterate over all possible starting positions of the submatrix
        for (int i = 0; i <= n - k; i++)
        {
            for (int j = 0; j <= n - k; j++)
            {
                int trace = 0;
                // Compute the trace for the submatrix starting at (i, j) of size kxk
                for (int l = 0; l < k; l++)
                {
                    trace += S[i + l][j + l];
                }
                // Update maximum trace if we found a new maximum
                maxTrace = max(maxTrace, trace);
            }
        }
    }
    cout << maxTrace << endl;
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