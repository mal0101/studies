#include"biblio.h"
int main() {
    int n = 60;
    int start = 42;
    cell* head =NULL;
    cell* survivor;


    head = create_circular_list(n);
    printf("The circular linked list:\n");
    print_list(head);


    survivor = josephus(head,  start);
    printf("The survivor using Josephus  is: %d\n", survivor->data);


    free(survivor);
    return 0;
}
