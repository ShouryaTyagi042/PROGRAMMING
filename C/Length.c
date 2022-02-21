#include <stdio.h>
// #include <cache÷.h>

int main() {
    char s[10000] ;
    printf("Enter a STRING : ");
    scanf("%s",s) ;
    int i = 0 ;
    while ( s[i] != '\0') {
        i++ ;
    }
    printf("Length of string is %d" , i ) ;

}
