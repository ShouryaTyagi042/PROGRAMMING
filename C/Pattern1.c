#include <stdio.h>
void myfunc(int x) {
    if (x>0) {
        myfunc(x-1) ;
        printf("%d",x) ;
        myfunc(x-1) ;
    }
    return;
 }
 int main() {
    myfunc(3) ;
    return 0;
}

