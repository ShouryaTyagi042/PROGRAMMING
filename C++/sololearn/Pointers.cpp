#include <bits/stdc++.h>
using namespace std ;

int main() {
    int x = 5 ;
    int *p = &x ;
    string food = "Pizza";  // Variable declaration
    string* ptr = &food;    // Pointer declaration

// Reference: Output the memory address of food with the pointer (0x6dfed4)
    cout << ptr << "\n";

// Dereference: Output the value of food with the pointer (Pizza)
    cout << *ptr << "\n";
}
