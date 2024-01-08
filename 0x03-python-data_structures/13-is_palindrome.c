#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer of function
 * Return: 1 if it is a palindrome or 0 if not
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (verify_palindrome(head, *head));
}

/**
 * verify_palindrome - function that verify if a linked list is a palindrome
 * @head: head of list
 * @end: head of list
 */

int verify_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (verify_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
