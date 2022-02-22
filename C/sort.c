#include<stdio.h>
int main(){
    int a,b;
    printf("size of array 1");
    scanf("%d",&a);
    int arr1[a];
    for(int i=0;i<a;i++){
        scanf("%d",&arr1[i]);
    }
    printf("size of array 2");
    scanf("%d",&b);
    int arr2[b];
    for(int i=0;i<b;i++){
        scanf("%d",&arr2[i]);
    }
    //sorting array1
    for(int i=1;i<a;i++){
        int current = arr1[i];
        int j=i-1;
        while(arr1[j]>current && j>=0){
            arr1[j+1]=arr1[j];
            j--;
        }
        arr1[j+1]=current;
    }
    //for(int i=0;i<a;i++){
        //printf("%d",arr1[i]);
    //}
        //soring array2
        for(int i=1;i<b;i++){
        int current1 = arr2[i];
        int j=i-1;
        while(arr2[j]>current1 && j>=0){
            arr2[j+1]=arr2[j];
            j--;
        }
        arr2[j+1]=current1;
        }
        if(a==b){
        for(int i=0;i<a;i++){
            if(arr1[i]==arr2[i]){
                printf("array are equal");
            }
            else{
                printf("arrays are not equal");
            }
        }
        }
        else{
            printf("arrays are not equal");
        }
    return 0;
}
