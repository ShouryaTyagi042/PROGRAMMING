#include<stdio.h>

int main()
{
    int i,j,k,l, num;
    for (i = 1; i <= 15; i++)
    {
        for ( l = 1; l <= 10-i; l++)
        {
            printf(" ");
        }

        num=1;
        for ( j = 1; j <= i; j++)
        {
            if(num<10)
              {
                  printf("%d", num);
                num++;
              }
              else{
                  num=0;
                  printf("%d", num);
                  num++;
              }
        }
        num=num-2;
        for ( k = 1; k <= i-1; k++)
        {
            if(num<0)
            {
                num=9;
                printf("%d", num);
                num--;
            }
            else{
            printf("%d", num);
            num--;}
        }
        printf("\n");

    }

    return 0;
}
