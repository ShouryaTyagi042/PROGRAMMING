#include<stdio.h>
#include<string.h>
int main(){
    char name1[30];
    char item1[20];
    char outlet1[30];
    printf("Enter the name of consumer :");
    scanf("%[^\n]s",&name1);
    printf("Enter the name of item :");
    scanf("%[^\n]s",&item1);
    printf("Enter the name of outlet :");
    scanf("%[^\n]s",&outlet1);
    FILE *ptr = NULL;
    char str[200];
    ptr = fopen("letter.txt","r");
    fscanf(ptr,"%[^\n]s",str);
    ptr=fopen("letter.txt","a");
    strcpy("name1[]","{name}");
    strcpy("item1[]","{item}");
    strcpy("outlet[]","{outlet}");
    ptr=fopen("letter.txt","a");
//  fprintf(ptr,"%s",str);
    printf("%s",str);

    return 0;
}
