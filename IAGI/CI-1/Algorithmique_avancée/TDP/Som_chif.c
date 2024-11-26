#include <stdio.h>

int Som_chif(int n) {
    int r, s = 0;
    while (r !=0) {
        r = n % 10;
        n /= 10;
        s += r;
    }
}