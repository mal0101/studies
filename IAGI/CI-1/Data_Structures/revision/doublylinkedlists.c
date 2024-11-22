#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* next;
    struct node* prev;
} node;

struct node* head;
struct node* getnewnode(int x) {
    /** struct node Mynode; local variable
    Mynode.data = x;
    Mynode.next = NULL;
    Mynode.prev = NULL; static part of the memory
    for the heap part of the memory: **/
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->data=x;
    newNode->prev=NULL;
    newNode->next=NULL;
    return newNode;
}
void insertathead(int x) {
    struct node* newnode = getnewnode(x);
    if (head == NULL) {
        head = newnode;
        return;
    }
    head->prev=newnode;
    newnode->next=head;
    head=newnode;
}
// the print function is the same for both singly and doubly linked lists, check the linkeslists.c file
void ReversePrint() {
    struct node* temp = head;
    if (temp == NULL) return; // if empty list, exit
    // Going to last Node
    while (temp->next != NULL) {
        temp = temp->next;
    }
    // Traversing backward using prev pointer
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->prev;
    }
    printf("\n");
}
// Inserting at tail
void insertattail(int x) {
    struct node * temp = head;
    struct node* newnode = getnewnode(x);
    if (head == NULL) {
        head = newnode;
        return;
    }
    while (temp->next !=NULL) {
        temp = temp->next;
    }
    temp->next = newnode;
    newnode->prev = temp;
}
int main() {
    head = NULL; // empty list
    insertathead(2);
    insertathead(4);
    insertathead(6);
    insertathead(8);
    insertattail(10);
    insertattail(12);
    ReversePrint();
    return 0;
}