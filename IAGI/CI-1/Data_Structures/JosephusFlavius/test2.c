#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;   // Index of the person
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

Node* findNodeAtIndex(Node* head, int targetIndex) {
    Node* current = head;
    while (current->data != targetIndex) {
        current = current->next;
    }
    return current;
}

void dynamicIndexJosephus(Node** head, int startIndex) {
    // Find the starting node at the specified index
    Node* current = findNodeAtIndex(*head, startIndex);
    Node* prev = NULL;

    // Continue until only one node remains
    while (current->next != current) {
        // Find the previous node
        prev = current;
        while (prev->next != current) {
            prev = prev->next;
        }

        // The elimination step is the killer's index
        int eliminationStep = current->data + 1;

        // Move to find the victim
        for (int i = 0; i < eliminationStep; i++) {
            prev = current;
            current = current->next;
        }

        // Print who kills whom
        printf("Person %d (index %d) kills person %d (index %d)\n", 
               prev->data, prev->data, current->data, current->data);

        // Remove the current node (victim)
        prev->next = current->next;
        free(current);
        
        // Move to the next killer
        current = prev->next;

        // Break if only one node remains
        if (current->next == current) {
            break;
        }
    }

    printf("The survivor is %d\n", current->data);
    *head = current;
}

int main() {
    int totalPeople = 60;  // Total number of people
    int startIndex = 42;   // Start killing from index 42

    Node* head = createCircularLinkedList(totalPeople);

    // Call the dynamic index-based Josephus function
    dynamicIndexJosephus(&head, startIndex);

    // Free the last remaining node
    free(head);

    return 0;
}