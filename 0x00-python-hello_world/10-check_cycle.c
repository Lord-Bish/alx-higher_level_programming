#include "lists.h"

/* Definition for singly-linked list */
struct listint_t {
    int data;
    struct listint_t* next;
};

typedef struct listint_t listint_t;

int check_cycle(listint_t *list) {
    if (list == NULL || list->next == NULL) {
        return 0;  /* No cycle if the list is empty or has only one node */
    }

    listint_t *slow = list;
    listint_t *fast = list->next;

    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) {
            return 1;  /* Cycle detected */
        }
        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;  /* No cycle found */
}

int main() {
    /* Example usage */
    int result;

    listint_t *head = NULL;
    head = (listint_t*)malloc(sizeof(listint_t));
    head->data = 1;
    head->next = NULL;

    listint_t *node2 = (listint_t*)malloc(sizeof(listint_t));
    node2->data = 2;
    node2->next = NULL;

    listint_t *node3 = (listint_t*)malloc(sizeof(listint_t));
    node3->data = 3;
    node3->next = NULL;

    head->next = node2;
    node2->next = node3;
    /* Uncomment the following line to create a cycle */
    /* node3->next = head; */

    result = check_cycle(head);
    if (result) {
        printf("Cycle detected.\n");
    } else {
        printf("No cycle found.\n");
    }

    /* Clean up memory */
    free(node3);
    free(node2);
    free(head);

    return 0;
}
