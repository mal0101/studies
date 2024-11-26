#include "header.h"

int Josephus(node * head, int k) {
    if (head->next == head) {
        return head->data;
    }
    node * curr = head;
    for (int i = 1; i < k; i++) {
        curr = curr->next;
    }
    node * to_kill = curr->next;
    while (to_kill == curr) {
        curr = curr->next;
        to_kill = curr->next;
    }
    printf("%02d killed %02d\n", curr->data, to_kill->data);
    int k_new = to_kill->data;
    Delete2(&head, to_kill);
    return Josephus(head, k_new);
}

int main() {
    int n = 60, i;
    int arr[n];
    for (i = 0; i < n; i++) {
        arr[i] = i + 1;
    }
    node * head = arrayToLinkedList(arr, n);
    makeCircular(head);
    int k = Josephus(head, 42);
    printf("The number who will live is %d\n", k);
    return 0;
}
