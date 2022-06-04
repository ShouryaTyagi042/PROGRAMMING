# include <stdio.h>
# include <stdlib.h>
// Creating a node
struct node {
  int value;
  struct node *next;
};

// print the linked list value
void printLinkedlist(struct node *p) {
  while (p != NULL) {
    printf("%d ", p->value);
    p = p->next;
  }
}
int main() {
    int n ;
    printf("Size of array: ");
    scanf("%d",&n) ;
    int arr[n] ;
    for (int i = 0; i < n; ++i)
    {
        scanf("%d",&arr[i]) ;
    }
    struct node *headNode, *currentNode, *temp;
    for (int i = 0; i < n; i++)
    {

        currentNode = malloc(sizeof(struct node));
        currentNode->value = arr[i] ;

        if (i == 0)
        {
            headNode = temp = currentNode;
        }
        else
        {
            temp->next = currentNode;
            temp = currentNode;
        }
    }

    temp->next = NULL;
    temp = headNode;
    printLinkedlist(headNode) ;
}
