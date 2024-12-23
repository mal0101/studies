#include "header.h"

int maxLinkedList(node * head) {
    int maxx = head->val;
    node * temp = head;
    if (head == NULL) {
        exit(1);
    }
    if (head->next == NULL) {
        return maxx;
    }
    while (temp != NULL) {
        if (temp->val > maxx) {
            maxx = temp->val;
        }
        temp = temp->next;
    }
    return maxx;
}


int main() {
   int array[] = {12345; 89052; 123456789; 90; 0; 100};
   printf("le maximum de la liste chainée est %d \n", maxLinkedList(array2LinkedList(array, 6)));
}