# include <bits/stdc++.h>

class employee {
    char name[80] ;
    public :
    void get_name(char *n) ;
    public :
    void put_name(char *n) ;
};
void employee :: put_name(char*n) {
    strcpy(name,n) ;
}

void employee :: get_name(char *n) {
     name ;
}
int main() {
    employee ted ;
    char name1[80] ;
    ted.put_name("TED") ;
    ted.get_name(name1) ;
    cout << name1 ;
}
