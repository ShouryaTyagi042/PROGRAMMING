#include<stdio.h>
#include<math.h>
bool prime(int n){
    if (n <= 3) {
        return true;
    }
    for(int i=2;i<=n/2;i++){
        if(n%i==0){
            return false;
        }

    }
    return 1;
}
int main(){
    int x;
    int n;
    printf("enter no. to be checked");
    scanf("%d",&x);
    printf("enter n till we have to find prime no.s: ");
    scanf("%d",&n);
    int result=prime(x);
    if(result==-1){
        printf("not prime\n");
    }
    else{
        printf(" prime\n");
    }
    for(int i=2;i<=n;i++){
        int result1=prime(i);
        if(result1==0){
            printf("%d is prime\n",i);
        }
        else{
            printf("%d is not prime\n",i);
        }
    }
    return 0;
}
