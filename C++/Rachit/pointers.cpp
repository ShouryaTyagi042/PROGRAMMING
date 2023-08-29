#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#define MAX 10000
using namespace std;

void func(int *p)
{
    *p = *p + 1;
    p = NULL;
}

int main()
{
    int i = 10;
    int *p = &i;
    func(p);
    cout << *p;
}