#include"biblio.h"

cell* create_node(int data) {
    cell *nouv = (cell*)malloc(sizeof(cell));
    if (nouv == NULL) {
        printf("Erreur d'allocation de mémoire.\n");
        exit(1);
    }
    nouv->data = data;
    nouv->next = NULL;
    return nouv;
}

cell* insert_node(cell* head, int data)
 {
    cell* nouv = create_node(data);

    if (head == NULL) {
        return nouv;
    }


    cell* temp = head;
    while (temp->next != head) {
        temp = temp->next;
    }

    temp->next = nouv;
    nouv->next = head;

    return head;
}
cell* create_circular_list(int n) {
    cell* head = NULL;
    cell* temp = NULL;
    cell* nouv = NULL;
    for (int i = 1; i <= n; i++) {
        nouv = create_node(i);
        if (!head) {
            head = nouv;
            temp = head;
        } else {
            temp->next = nouv;
            temp = nouv;
        }
    }
    temp->next = head;
    return head;
}
void print_list(cell* head) {
    if (head == NULL) {
        printf("The list is empty.\n");
        return;
    }

    cell* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(head)\n");
}

cell* josephus(cell* head, int start) {

    cell* current = head;
    cell* prev = NULL;
    if (head == NULL || start <= 0)
        return NULL;


    while (current->data != start) {
        current = current->next;
    }

    current = current->next;
    while (current->next != current) {
        for (int i = 1; i < start; i++) {
            prev = current;
            current = current->next;
        }



        printf("Removing: %d\n", current->data);
        prev->next = current->next;
        free(current);


        current = prev->next;


        start = current->data;
        current = current->next;
    }

    return current;
}