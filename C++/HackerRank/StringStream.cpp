#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    // Complete this function
    vector<int> v ;
    stringstream s(str) ;
    int num ;
    char com ;
    while(s >> num  ){
        v.push_back(num) ;
        s >> com ;
    }
    return v ;



}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}
