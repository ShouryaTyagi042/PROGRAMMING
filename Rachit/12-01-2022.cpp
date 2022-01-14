#include <bits/stdc++.h>

int main() {
    int n;
    scanf("%d",&n);
    int alpha =64;
    for(int i =1;i<=n;i++){
        //int alpha =65;
        alpha+=i;
        //int alpha =65;
        //char alpha ='A';
        for(int j=1; j<=n;j++){
            if(j<=n-i){
                printf(" ");
            }
            else {
                //alpha+=i-1;
                printf("%c",alpha);
                alpha--;
            }
        }
        printf("\n");
    }
    return 0;
}
