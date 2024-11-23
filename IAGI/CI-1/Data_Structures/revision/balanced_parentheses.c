/* in this program we will implement a stack to check if the parentheses in a string are balanced or not */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    char data;
    struct node* next;
} node;

struct node * top = NULL;

void Push(char x) {
    struct node * temp  = (struct node *)malloc(sizeof(struct node));
    temp->data = x;
    temp->next = top;
    top = temp;
}

void Pop(){
    struct node * temp;
    if (top == NULL) return;
    temp = top;
    top = top->next;
    free(temp);
}

char Top() {
    return top->data;
}

int IsEmpty() {
    return top == NULL;
}

int check4balancedparentheses(char *exp) {
    for (int i = 0; i<strlen(exp); i++) {
        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[') {
            Push(exp[i]);
            }
        else if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']') {
            if (IsEmpty()) return 0;
            char c = Top();
            if (exp[i] == ')' && c == '(') Pop();
            else if (exp[i] == '}' && c == '{') Pop();
            else if (exp[i] == ']' && c == '[') Pop();
            else return 0;
        }
    }
}
