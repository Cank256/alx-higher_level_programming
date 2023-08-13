#include "lists.h"

int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
        return (1); // An empty list is considered a palindrome

    listint_t *slow = *head, *fast = *head, *prev = NULL;

    // Find the middle of the list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        listint_t *next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    if (fast != NULL) // Odd number of elements, skip the middle element
        slow = slow->next;

    // Compare the reversed first half with the second half
    while (prev != NULL && slow != NULL)
    {
        if (prev->n != slow->n)
            return (0); // Not a palindrome

        prev = prev->next;
        slow = slow->next;
    }

    return (1); // It is a palindrome
}
