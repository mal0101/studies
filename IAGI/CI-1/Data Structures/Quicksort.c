#include <stdio.h>

void permuter(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int *tab, int debut, int fin) {
    int pivot = tab[fin];
    int i = debut - 1;
    for (int j = debut; j < fin; j++) {
        if (tab[j] < pivot) {
            i++;
            permuter(&tab[i], &tab[j]);
        }
    }
    permuter(&tab[i + 1], &tab[fin]);
    return i + 1;
}

void quicksort(int *tab, int debut, int fin) {
    if (debut < fin) {
        int pivot = partition(tab, debut, fin);
        quicksort(tab, debut, pivot - 1);
        quicksort(tab, pivot + 1, fin);
    }
}

int main() {
    int tab[] = {5, 2, 9, 4, 7, 6, 1, 3, 8};
    int n = sizeof(tab) / sizeof(tab[0]);
    quicksort(tab, 0, n - 1);
    for (int i = 0; i < n; i++) {
        printf("%d ", tab[i]);
    }
    return 0;
}