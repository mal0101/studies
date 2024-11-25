#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// all operations for queues are if constant time
typedef struct node {
    int data;
    struct node *left;
    struct node *right;
    struct node *next;
} node;

void levelorder(node * root) {
    if (root == NULL) return;
    node * queue = NULL;
    node * temp = root;
    while (temp) {
        printf("%d", temp->data);
        if (temp->left) {
            queue = temp->left;
        }
        if (temp->right) {
            queue = temp->right;
        }
        temp = temp->next;
        pop(queue);
    }
}
void preoder(node * root) {
    if (root == NULL) return;
    printf("%d", root->data);
    preorder(root->left);
    preorder(root->right);
}
void inorder(node * root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d", root->data);
    inorder(root->right);
}
void postorder(node* root) {
    if (root == NULL) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d", root->data); 
}
int main() {

}