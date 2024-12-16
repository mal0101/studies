#include "biblio.h"

// Exercice 1: Maximum d'une liste chainée

int maxLinkedList(node * head) {
    int max = head->data;
    while (head != NULL){
        if (head->data > max) {
            max = head->data;
        }
        head = head->next;
    }
}

int maxLinkedListRec(node * head) {
    if (head == NULL) {
        return 0;
    }
    int max = maxLinkedListRec(head->next);
    if (head->data > max) {
        return head->data;
    }
    return max;
    // return ((head->data > max)) ? head->data : max;
}

// Exercice 2: Concaténer deux listes chainées

void concatLinkedLists(node*head1, node*head2) {
    if (head1 == NULL) {
        head1 == head2;
        return;
    }
    while (head1->next!=NULL){
        head1 = head1->next;
    }
    head1->next=head2;
}

// Exercice 3: 

void extract_from_Linked_list(node * head, node ** pheadpos, node ** pheadneg) {
    node * pos = NULL;
    node * neg = NULL;
    node ** posparser = pheadpos;
    node ** negparser = pheadneg;
    while (head != NULL) {
        if (head->data >= 0) {
            *posparser = createNode(head->data);
            posparser = &((*posparser)->next);
        }
        else {
            *negparser = createNode(head->data);
            negparser = &((*negparser)->next);
        }
        head = head->next;
    }
    *posparser = NULL;
    *negparser = NULL;
}

// Helper function to create a new node
node* createNode(int data) {
    node* newNode = (node*)malloc(sizeof(node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Helper function to print a linked list
void printLinkedList(node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

/** int main() {
    // Create a linked list: 1 -> -2 -> 3 -> -4 -> 5 -> NULL
    node* head = createNode(1);
    head->next = createNode(-2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(-4);
    head->next->next->next->next = createNode(5);

    // Print the original linked list
    printf("Original linked list:\n");
    printLinkedList(head);

    // Create pointers for positive and negative lists
    node* posHead = NULL;
    node* negHead = NULL;

    // Extract positive and negative lists
    extract_from_Linked_list(head, &posHead, &negHead);

    // Print the positive and negative linked lists
    printf("Positive linked list:\n");
    printLinkedList(posHead);
    printf("Negative linked list:\n");
    printLinkedList(negHead);

    return 0;
}
*/

// Exercice 4: Permuter deux places d'une liste (TO REDO)
void permuter_positions(node ** head, node * v, node * t) {
    node * prev_V = NULL, *prev_T = NULL, *current = *head;
    if (t == v)
        return;
    while (current != NULL && (prev_T == NULL || prev_V == NULL)) {
        if (current->next == t) 
            prev_T = current;
        if (current->next == v)
            prev_V = current;
        current = current->next;
    }
    if (prev_T != NULL)
        prev_T->next = v;
    else if (prev_V != NULL)
        prev_V->next = t;

    node * temp = v->next;
    v->next = t->next;
    t->next = temp;
    
    if (*head == t)
        *head = v;
    else if (*head == v)
        *head = t;
}
/** int main() {
// Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
node* head2 = createNode(1);
head2->next = createNode(2);
head2->next->next = createNode(3);
head2->next->next->next = createNode(4);
head2->next->next->next->next = createNode(5);

// Print the original linked list
printf("Original linked list:\n");
printLinkedList(head2);

// Nodes to be swapped
node* v = head2->next; // Node with value 2
node* t = head2->next->next->next; // Node with value 4

// Swap the nodes
permuter_positions(&head2, v, t);

// Print the modified linked list
printf("Modified linked list after swapping nodes 2 and 4:\n");
printLinkedList(head2);
}
**/
// Exercice 5: Supprimer des élémements
// Fonction 1: supprimer toutes les occurences d'un élément donné x
void supprimer_all_occurences(node ** head, int x) {
    node * current = * head;
    node * prev = NULL;
    while (current != NULL) {
        if (current->data == x) {
            if (prev == NULL) {
                *head = current->next;
                free(current);
                current = *head;
            }
            else {
                prev->next = current->next;
                free(current);
                current = prev->next;
            }
            }
        else {
            prev = current;
            current = current->next;
            }
        }
    }  

// Fonction 2: Supprimer toutes les k+1 occurences de x

void supprimer_after_k_occurences(node ** head, int k, int x) {
    node * current =  * head;
    int count = 0;
    while (current != NULL) {
        if (current->data == x) {
            count ++;
        }
        if (count == k) {
                supprimer_all_occurences(&(current->next), x);
                break;
        }
        current = current->next;
    }
}

// Fonction 3: pour xhaque élément de la liste on ne laisse que sa première occurence
void supprimer_after_first_occurence(node ** head, int x) {
    node * current = *head;
    while (current != NULL) {
        if (current->data == x) {
            supprimer_all_occurences(&(current->next), x);
        }
        current = current->next;
    }
}

// Exercice 6: Inverser une liste:

void inverser_linked_list(node ** head) {
    node * prev = NULL;
    node * current = * head;
    node * suiv = NULL;
    while (current != NULL) {
        suiv = current->next;
        current->next = prev;
        prev = current;
        current= suiv;
    }
    *head = prev;
}
// Exercice 7: Refermer une lise chainée
void refermer_linked_list(node ** head) {
    node * current = * head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = head;
}

// Function that prints circular linked list:
 void print_circular_linked_list(node * head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    node * current = head;
    do {
        printf("%d -> ", current->data);
        current = current->next;
    } while (current != head);
    printf("NULL\n");
} 


// Exercice 8: Saisir, enregistrer puis évaluer un polynome (TO REDO)
// Fonction 1: Construction de la liste sur la base des coefficients et des exposants, siaisis au clavier

void saisir_polynome(node ** head) {
    int coef, exposant;
    while (1) {
        printf("Saisir le coefficient et l'exposant du terme du polynome (0, 0 pour terminer): ");
        scanf("%d %d", &coef, &exposant);
        if (coef == 0 && exposant == 0) break;
        node * current = * head;
        node * prev = NULL;
        while (current != NULL && current->data > exposant){
            prev = current;
            current = current->next;
        }
        if (current == NULL) {
            if (prev == NULL) {
                *head = createNode(exposant);
                (*head)->next = createNode(coef);
            }
            else {
                prev->next = createNode(exposant);
                prev->next->next = createNode(coef);
            }
            }
        else if (current->data == exposant) {
            current->next->data += coef;
        }
        else {
            if (prev == NULL) {
                *head = createNode(exposant);
                (*head)->next = createNode(coef);
                (*head)->next->next = current;
            }
            else {
                prev->next = createNode(exposant);
                prev->next->next = createNode(coef);
                prev->next->next->next = current;
            }
        }
    } 
    printf("Polynome saisi avec succès\n");
    printLinkedList(*head);
    
}
// Fonction 2: Evaluation du polynome en un point donné

// Exercice 9: Créer une liste circulaire ordonnée à partir d'un tableau non ordonné d'entiers

void create_ordered_circular_linked_list(node ** head, int * tab, int n) {
    for (int i = 0; i < n; i++) {
        node * current = * head;
        node * prev = NULL;
        while (current != NULL && current->data < tab[i]) {
            prev = current;
            current = current->next;
        }
        if (current == NULL) {
            if (prev == NULL) {
                *head = createNode(tab[i]);
                (*head)->next = *head;
            }
            else {
                prev->next = createNode(tab[i]);
                prev->next->next = *head;
            }
        }
        else {
            if (prev == NULL) {
                *head = createNode(tab[i]);
                (*head)->next = current;
                node * temp = current;
                while (temp->next != current) {
                    temp = temp->next;
                }
                temp->next = *head;
            }
            else {
                prev->next = createNode(tab[i]);
                prev->next->next = current;
            }

        }

    }

}


// Exercice 10: Réaliser le chaînage arrière d’une liste doublement chaînée

void chainage_arriere(node ** head) {
    node * current = * head;
    while (current->next != NULL) {
        current = current->next;
    }
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->prev;
    }
    printf("NULL\n");
}

// Main function to test the above functions



 int main () {
    // Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    node* head = createNode(3);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);
    head->next->next->next->next = createNode(5);
    head->next->next->next->next->next = createNode(3);
    head->next->next->next->next->next->next = createNode(6);
    head->next->next->next->next->next->next->next = createNode(3);
    head->next->next->next->next->next->next->next->next = createNode(7);
    head->next->next->next->next->next->next->next->next->next = createNode(3);

    // Print the original linked list
    printf("Original linked list:\n");
    printLinkedList(head);

    // Remove all occurrences of 3
    // supprimer_all_occurences(&head, 3);
    // supprimer_after_k_occurences(&head, 2, 3);
    // supprimer_after_first_occurence(&head, 3);
    // inverser_linked_list(&head);
    //refermer_linked_list(&head);
    // Print the modified linked list
    printf("Modified linked list: \n");
    // print_circular_linked_list(head);

    return 0;

/**     node* head = NULL;
    saisir_polynome(&head);
    return 0;

    node* head = NULL;
    int tab[] = {5, 3, 7, 2, 1, 4, 6};
    int n = sizeof(tab) / sizeof(tab[0]);
    create_ordered_circular_linked_list(&head, tab, n);
    print_circular_linked_list(head);
    */
    return 0;
}