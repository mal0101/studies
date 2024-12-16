#ifndef biblio_h
#define biblio_h
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

// node type definition

typedef struct node {
    int data;
    struct node * next;
} node;

// in this file we will define functions to be used for problems related to linked lists
int maxLinkedList(node * head);
int maxLinkedListRec(node * head);
void concatLinkedLists(node * head1, node * head2);
void extract_from_Linked_list(node * head, node ** pheadpos, node ** pheadneg);
node* createNode(int data);
void printLinkedList(node* head);
void permuter_positions(node ** head, node * v, node * t);
void supprimer_all_occurences(node **head, int x);
void supprimer_after_k_occurences(node ** head, int k, int x);
void supprimer_after_first_occurence(node ** head, int x);
void inverser_linked_list(node **head);
void refermer_linked_list(node ** head);
void print_circular_linked_list(node *head);
void saisir_polynome(node ** head);
void evaluer_polynome(node * head, int x);


#endif