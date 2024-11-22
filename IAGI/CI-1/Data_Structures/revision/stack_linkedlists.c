#include <stdio.h>
#include <stdlib.h>

// Stack can be implemented using array or linked list
// In Linked List Implementation:
// push and pop operations are O(1) for both
// insert and delete from head are O(1) therefore the head is considered the top of the stack

typedef struct node {
    int data;
    struct node* next;
} node;

struct node * top = NULL;
void Push(int x) {
    struct Node * temp  = (struct node *)malloc(sizeof(struct node *));
    temp->data = x;
    temp->next=top;
    top = temp;
}
void Pop(){
    struct node * temp;
    if (top == NULL) return;
    temp = top;
    top = top->next;
    free(temp);
}
void Top() {
    printf("%d\n", top->data);
}
