#include "_TD-01.h"

int JosephAlivePos(Node* head, int k)
{
    if (head->next == head->next->next)
        return head->value;
    Node* curr = getListNodeAt(head, k-1);
    Node* next = curr->next;
    printf("[SOS] %02d killed %02d\n", k, curr->value);
    int newK = curr->value;
    popListNode(curr);
    return JosephAlivePos(next, newK);
}

void testJosephAlivePos()
{
    int n = 60, i;
    int arr[n];
    for (i = 0; i < n; i++) {
        arr[i] = i+1;
    }
    Node* head = arrayToLinkedList(arr, n);
    convertToCycle(head);
    int k = JosephAlivePos(head, 42);
    printf("The number who will live is %d\n", k);
}