#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* next;
} node;

struct node* head;

// insert node at beginning
void insert(int x) {
    node *temp = (node*)malloc(sizeof(struct node));
    temp->data = x;
    temp->next= NULL;
    temp->next = head;
    head = temp;
}

// insert at the nth position
void insertn(int x, int n) {
    struct node* temp1 = (struct node*)malloc(sizeof(struct node));
    temp1->data=x;
    temp1->next=NULL;
    if (x == 1) {
        temp1->next=head;
        head = temp1;
        return;
    }
    struct node* temp2 = head;
    for (int i = 0; i < n-2; i++) {
        temp2 = temp2->next;
    }
    temp1->next = temp2->next; // temp1 points to n+1
    temp2->next = temp1; // n-1 points to temp1
}

// delete at nth position
void delete(int n){
    struct node * temp1 = head;
    if (n == 1) {
        head = temp1->next;
        free(temp1);
        return;
    }
    int i;
    for(i=0;i<n-2;i++){
        temp1 = temp1->next;
    }
    struct node * temp2 = temp1->next;
    temp1->next = temp2->next; // n-1 points to n+1
    free(temp2); // deletes temp2
}

// reverse a linked list
struct Node* reverse() {
    struct node * current, * prev, * next;
    current = head;
    prev = NULL;
    while (current != NULL) {
        current = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
    return head;
}

// reverse linked list recursively
void reverse(struct node * head){
    if (head == NULL) return; // exit condition
    reverse(head->next); // recursive call
    printf("%d", head->data);
}

// print iteratively
void Print() {
    struct node* temp = head;
    while (temp != NULL) {
        printf("%d", temp->data);
        temp=temp->next;
    }
    printf("\n");
}

// print recursively
void printrec(struct node* head){
    if (head == NULL) return; // exit condition
    printf("%d", head->data);// First print the value in the node
    printrec(head->next); // recursive call
}

int main() {
    head = NULL;
    printf("How many numbers?\n");
    int n, i, x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Enter the number\n");
        int x;
        scanf("%d", &x);
        insert(x);
        Print();
    }
}
