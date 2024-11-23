#include <stdio.h>
#include <stdlib.h>

void reverse(char C[], int n) {
    char *stack = (char*)malloc(n*sizeof(char));
    for (int i = 0; i < n; i++) {
        stack[i] = C[i];
    }
    for (int i = 0; i < n; i++) {
        C[i] = stack[n-i-1];
    }
} // the complexity of this function is O(n), both time and space complexities are equal
int main() {
    char C[] = "12345";
    reverse(C, 5);
    printf("%s\n", C);
    return 0;
}