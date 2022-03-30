#include <stdio.h>
struct date
{
    int day ;
    int month ;
    int year ;

};


int main() {
    struct date date1 , date2 ;
    scanf("%d %d %d",&date1.day,&date1.month,&date1.year) ;
    scanf("%d %d %d",&date2.day,&date2.month,&date2.year) ;

    if (date1.day == date2.day) {
        printf("equal") ;
    }
    return  0;


}
