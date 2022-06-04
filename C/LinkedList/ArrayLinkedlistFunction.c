# include <stdio.h>
# include <stdlib.h>

struct node {
    int data ;
    struct node * next ;
} ;

void printLinkedlist(struct node *p) {
  while (p != NULL) {
    printf("%d ", p->data);
    p = p->next;
  }
}

struct node * array_linkedlist(struct node * head  ){
    int arr[] = {1,2,3,4,6} ;
    struct node * temp = head ;
    int i ;
    for ( i = 0 ; i < 5 ; i++) {
        struct node * currentNode = malloc(sizeof(struct node)) ;
        currentNode -> data = arr[i] ;
        if (i == 0) {
            head = temp = currentNode ;
        }
        else {
            temp -> next = currentNode ;
            temp = currentNode ;
        }
        // temp -> next = NULL ;

    }
    temp->next = NULL;
    temp = head;
    return head;
}
int main() {
    int arr[] = {1,2,3,4,5} ;
    struct node * start ;
    struct node * head = malloc(sizeof(struct node)) ;
    head  = array_linkedlist(start) ;
    printLinkedlist(head) ;
}
