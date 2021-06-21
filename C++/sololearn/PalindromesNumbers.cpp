#include <bits/stdc++.h>
using namespace std;

int isPalindrome(int x) {
    //complete the function
    int y = x ;
    int rev = 0 ;
    while (x>0) {
        rev = rev * 10 + x % 10 ;
        x = x / 10 ;
    }
    // cout << rev << endl;
    if (rev == y){
        return 1 ;

    }
    else {
        return 0 ;
    }




}

int main() {
    int n;
    cin >>n;
    // cout<<isPalindrome(n) ;
    // isPalindrome(n) ;

    if(isPalindrome(n)==1) {
        cout <<n<<" is a palindrome";
    }
    else {
        cout << n<<" is NOT a palindrome";
    }
    return 0;
}
