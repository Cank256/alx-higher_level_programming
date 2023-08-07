#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *tortoise, *hare;

    if (!list)
        return (0);

    tortoise = list;
    hare = list;

    while (hare != NULL && hare->next != NULL)
    {
        tortoise = tortoise->next;          // Tortoise moves one step
        hare = hare->next->next;            // Hare moves two steps

        if (tortoise == hare)               // If they meet, then there's a cycle
            return (1);
    }

    return (0);                             // If we've gone through the whole list without the pointers meeting, no cycle
}
