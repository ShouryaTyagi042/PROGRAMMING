#include <iostream>
using namespace std;
int search(int arr[],int start,int end,int num){
    if(start<=end){
        int mid = start+(end+1)/2;
        if(arr[mid]==num){
            return mid;
        }
        if(arr[mid]>num){
            return search(arr,start,mid-1,num);
        }
        if(arr[mid]<num){
            return search(arr,mid+1,end,num);
        }

    }
    return -1;
}

int main(void){
    int myarr[3]={1,2,3};
    int n=4;
    int result= search(myarr,0,2,n);
    cout<<result<< "\n";

    return 0;

}
