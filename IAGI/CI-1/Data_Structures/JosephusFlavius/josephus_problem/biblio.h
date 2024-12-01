#ifndef BIBLIO_H_INCLUDED
#define BIBLIO_H_INCLUDED

#include<stdio.h>
#include<stdlib.h>
typedef struct cel {

    int data ;
    struct cel *next ;

}cell;
cell* create_node(int );
cell* insert_node(cell* head, int data);
cell* create_circular_list(int n);
void print_list(cell* head);
cell* josephus(cell* head, int start) ;


#endif // BIBLIO_H_INCLUDED
