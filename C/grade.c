#include <stdio.h>

int main() {
    int marks ;
    scanf("%d",&marks) ;
    //85 a+
    //75 - 84 a
    //65 - 74 b
    //50 - 64 c
    // <50 d
    if ( marks >= 85) {
        printf("Your Grade is A+ ") ;
    }
    if (marks >= 75 && marks < 85 ) {
        printf("Your Grade is A ") ;
    }
    if ( marks >= 65 && marks < 75 ) {
        printf("Your Grade is B ") ;
    }
    if (marks >= 50 && marks < 65) {
        printf("Your Grade is C ") ;
    }
    if (marks < 50 ) {
        printf("Your Grade is D ") ;
    }

}
