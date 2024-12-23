#include "header.h"

int max(int a, int b) {
    return (a > b) ? a : b;
}
node * createNode(int val) {
    node * nodeptr = (node *)malloc(sizeof(node));
    nodeptr->val = val;
    nodeptr->next = NULL;
    return nodeptr;
}
node * array2LinkedList(int * array, int length) {
    if (length == 0) {
        return NULL;
    }
    node * head = createNode(array[0]);
    node * temp = head;
    for (int i = 1; i < length; i++)
    {
        temp->next = createNode(array[i]);
        temp = temp->next;
    }
    return head;
}

node * array2CircularLinkedList(int * array, int length) {
    if (array == NULL || length == 0) {
        return NULL;
    }
    node * head = createNode(array[0]);
    node * temp = head;

    for (int i = 1; i < length; i++) {
        temp->next = createNode(array[i]);
        temp = temp->next;
    }
    temp->next = head;
    return head;
}

