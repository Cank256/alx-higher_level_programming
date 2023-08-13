#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head node of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
if (head == NULL || *head == NULL)
{
return (1);
}

listint_t *slow = *head, *fast = *head, *prev = NULL;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
listint_t *next = slow->next;
slow->next = prev;
prev = slow;
slow = next;
}

if (fast != NULL)
{
slow = slow->next;
}

while (prev != NULL && slow != NULL)
{
if (prev->n != slow->n)
{
return (0);
}

prev = prev->next;
slow = slow->next;
}

return (1);
}
