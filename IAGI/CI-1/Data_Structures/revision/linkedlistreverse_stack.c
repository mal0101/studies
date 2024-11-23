#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* next;
} node;

struct node *top = NULL;

void push(int x) {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    temp->data = x;
    temp->next = top;
    top = temp;
}

void pop() {
    struct node *temp;
    if (top == NULL) return;
    temp = top;
    top = top->next;
    free(temp);
}

void Top() {
    if (top != NULL) {
        printf("%d\n", top->data);
    }
}

struct node* head = NULL;

void reverse() {
    if (head == NULL) return;
    struct node* temp = head;
    while (temp != NULL) {
        push(temp->data);
        temp = temp->next;
    }
    temp = head;
    while (temp != NULL) {
        temp->data = top->data;
        pop();
        temp = temp->next;
    }
}

void insert(int x) {
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = x;
    temp->next = head;
    head = temp;
}

void Print() {
    struct node* temp = head;
    printf("List is: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    insert(2);
    insert(4);
    insert(6);
    insert(5);
    Print();
    reverse();
    Print();
    return 0;
}
