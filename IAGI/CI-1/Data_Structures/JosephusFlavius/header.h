#ifndef HEADER_H
#define HEADER_H

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node* next;
} node;

struct node* head;

void Delete(int n){
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

void Delete2(node** head_ref, node* del) {
    if (*head_ref == NULL || del == NULL) return;

    // If the node to be deleted is the head node
    if (*head_ref == del) {
        *head_ref = del->next;
    }

    // Find the previous node of the node to be deleted
    node* temp = *head_ref;
    while (temp->next != del) {
        temp = temp->next;
    }

    // Unlink the node from the linked list
    temp->next = del->next;

    // Free memory
    free(del);
}

void Insert(int x) {
    node *temp = (node*)malloc(sizeof(struct node));
    temp->data = x;
    temp->next= NULL;
    temp->next = head;
    head = temp;
}

void Print() {
    struct node * temp = head;
    while (temp != NULL) {
        printf("%d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void makeCircular(node * head) {
    struct node * temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = head;
}

node * getListNodeAt(node * head, int index) {
    node * current = head;
    for (int i = 0; i < index; i++) {
        current = current->next;
    }
    return current;
}

node * arrayToLinkedList(int arr[], int n) {
    node * head = NULL;
    node * temp = NULL;
    node * p = NULL;

    for (int i = 0; i < n; i++) {
        temp = (node*)malloc(sizeof(node));
        temp->data = arr[i];
        temp->next = NULL;

        if (head == NULL) {
            head = temp;
        } else {
            p->next = temp;
        }
        p = temp;
    }
    return head;
}




#endif