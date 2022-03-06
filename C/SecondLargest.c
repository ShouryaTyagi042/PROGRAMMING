#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int max=arr[0];
    int min = arr[0] ;
    for (int i=1;i<n;i++){
        if(arr[i]>max){
            max=arr[i];
        }
        if (arr[i] < min) {
            min = arr[i] ;
        }
    }
    int max2 = min ;
    for(int i=0;i<n;i++){
        if(arr[i] != max ){
            if ( max2 < arr[i]) {
                max2 = arr[i] ;
            }
        }
    }
    printf("second largest element is %d",max2);
        return 0;
    }

