#include<stdio.h>
#include<string.h>
int main(){
    char s[100];
    //char s1[100];
    printf("enetr string");
    gets(s);
    int i;
    for( i=0;s[i]!='\0';i++){
}
char s1[i];
printf("%d\n",i);
    for(int j=0;j<i;j++){
        // printf("%c\n",s[j]);
        s1[j]=s[i-j-1];
    }
    printf("reverse string is %s",s1);
    return 0;
}

