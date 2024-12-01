#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

Node* createCircularLinkedList(int totalPeople) {
    Node* head = createNode(0);
    Node* current = head;
    for (int i = 1; i < totalPeople; i++) {
        current->next = createNode(i);
        current = current->next;
    }
    current->next = head;  // Make it circular
    return head;
}

void circularJosephus(Node** head, int k) {
    Node* current = *head;
    Node* prev = NULL;

    while (current->next != current) {
        for (int i = 0; i < k - 1; i++) {
            prev = current;
            current = current->next;
        }
        printf("Person %d is killed\n", current->data);
        prev->next = current->next;
        free(current);
        current = prev->next;
    }

    printf("The survivor is %d\n", current->data);
    *head = current;
}

int main() {
    int totalPeople = 60;  // Total number of people
    int k = 3;             // Step count for elimination

    Node* head = createCircularLinkedList(totalPeople);

    // Call the circular Josephus function
    circularJosephus(&head, k);

    // Free the last remaining node
    free(head);

    return 0;
}
