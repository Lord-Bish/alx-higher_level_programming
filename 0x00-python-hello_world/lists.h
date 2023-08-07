#ifndef _LISTS_H_
#define _LISTS_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct listint_t {
    int data;
    struct listint_t* next;
};

typedef struct listint_t listint_t;

#endif
