// Structure de la liste chainée:
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Exercice 1
// Fonction itérative pour trouver la valeur maximale dans la liste chainée
int max(Node* head) {
    int max = head->data;
    while (head != NULL) {
        if (head->data > max) {
            max = head->data;
        }
        head = head->next;
    }
    return max;
}

// Fonction récursive pour trouver la valeur maximale dans la liste chainée
int max_rec(Node* head) {
    if (head == NULL) {
        return -1;
    }
    int max = max_rec(head->next);
    return head->data > max ? head->data : max;
}

// Test 
int main() {
    Node* head = malloc(sizeof(Node));
    head->data = 3;
    head->next = malloc(sizeof(Node));
    head->next->data = 5;
    head->next->next = malloc(sizeof(Node));
    head->next->next->data = 2;
    head->next->next->next = NULL;

    printf("Valeur maximale (itératif): %d\n", max(head));
    printf("Valeur maximale (récursif): %d\n", max_rec(head));

    return 0;
}


// Exercice 2
// Attacher deux listes L1 et L2
void attach_lists(Node* L1, Node* L2) {
    if (L1 == NULL) {
        L1 = L2;
        return;
    }
    Node* current = L1;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = L2;
}

// Exercice 3
// Extraire deux listes à partir d'une liste
void split_list(Node* head, Node** positive_list, Node** negative_list) {
    *positive_list = NULL;
    *negative_list = NULL;
    Node* pos_tail = NULL;
    Node* neg_tail = NULL;

    while (head != NULL) {
        Node* new_node = malloc(sizeof(Node));
        new_node->data = head->data;
        new_node->next = NULL;

        if (head->data >= 0) {
            if (*positive_list == NULL) {
                *positive_list = new_node;
                pos_tail = new_node;
            } else {
                pos_tail->next = new_node;
                pos_tail = new_node;
            }
        } else {
            if (*negative_list == NULL) {
                *negative_list = new_node;
                neg_tail = new_node;
            } else {
                neg_tail->next = new_node;
                neg_tail = new_node;
            }
        }
        head = head->next;
    }
}

// Exercice 4
// Permuter deux places d’une liste

void swap_nodes(Node** head_ref, Node* t, Node* v) {
    if (t == v || t == NULL || v == NULL) {
        return; // No swap needed if they are the same node or either is NULL
    }

    // Find the previous nodes of `t` and `v`
    Node* prevT = NULL;
    Node* prevV = NULL;
    Node* current = *head_ref;

    while (current != NULL) {
        if (current->next == t) prevT = current;
        if (current->next == v) prevV = current;
        current = current->next;
    }

    // If `t` or `v` are not in the list, return
    if (prevT == NULL && *head_ref != t && *head_ref != v) return;
    if (prevV == NULL && *head_ref != t && *head_ref != v) return;

    // Adjust the previous pointers to point to the other node
    if (prevT != NULL) {
        prevT->next = v;
    } else {
        *head_ref = v;  // Update head if `t` was the head
    }

    if (prevV != NULL) {
        prevV->next = t;
    } else {
        *head_ref = t;  // Update head if `v` was the head
    }

    // Swap the `next` pointers of `t` and `v`
    Node* temp = t->next;
    t->next = v->next;
    v->next = temp;
}

// Exercice 5
// Supprimer des éléments de la liste

// Supprimer toutes les occurrences d’un élément donné x
void delete_all_occurrences(Node** head_ref, int x) {
    Node* current = *head_ref;
    Node* prev = NULL;

    while (current != NULL) {
        if (current->data == x) {
            if (prev == NULL) {
                *head_ref = current->next;
            } else {
                prev->next = current->next;
            }
            Node* temp = current;
            current = current->next;
            free(temp);
        } else {
            prev = current;
            current = current->next;
        }
    }
}

// Ne laisser que les k premières occurrences de x et supprimer les suivantes
void delete_after_k_occurrences(Node** head_ref, int x, int k) {
    Node* current = *head_ref;
    Node* prev = NULL;
    int count = 0;

    while (current != NULL) {
        if (current->data == x) {
            count++;
            if (count > k) {
                if (prev == NULL) {
                    *head_ref = current->next;
                } else {
                    prev->next = current->next;
                }
                Node* temp = current;
                current = current->next;
                free(temp);
                continue;
            }
        }
        prev = current;
        current = current->next;
    }
}

// Ne laisser que la première occurrence de chaque élément
void delete_duplicates(Node** head_ref) {
    Node* current = *head_ref;

    while (current != NULL) {
        delete_after_k_occurrences(&current->next, current->data, 0);
        current = current->next;
    }
}

// Exercice 6
// Inverser une liste


// Version itérative pour inverser une liste chaînée
void reverse_iterative(Node** head_ref) {
    Node* prev = NULL;
    Node* current = *head_ref;
    Node* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head_ref = prev;
}

// Version récursive pour inverser une liste chaînée
void reverse_recursive(Node** head_ref) {
    if (*head_ref == NULL || (*head_ref)->next == NULL) {
        return;
    }

    Node* rest = (*head_ref)->next;
    reverse_recursive(&rest);
    (*head_ref)->next->next = *head_ref;
    (*head_ref)->next = NULL;
    *head_ref = rest;
}

// Exercice 7
// Refermer une liste sur elle-même

void make_circular(Node* head) {
    if (head == NULL) {
        return;
    }

    Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = head;
}