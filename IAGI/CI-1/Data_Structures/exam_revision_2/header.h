#ifndef header_h
#define header_h

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node * next;
}node;

int max(int a, int b);
int maxLinkedList(node * head);
node * array2LinkedList(int * array, int length);
node * createNode(int val);
node * array2CircularLinkedList(int * array, int length);

#endif