#include <bits/stdc++.h>

using namespace std ;
int main() {
    int n, num ;
    cin >> n ;
    // std::vector<char> v;
    vector<int> v;
    for (int i = 0; i<n; i++ ) {
        cin >> num ;
        v.push_back(num) ;
    }
    sort(v.begin(),v.end()) ;
    for (int i=0; i<v.size(); i++) {
        cout << v[i] << " " ;
    }




    return 0 ;
}
