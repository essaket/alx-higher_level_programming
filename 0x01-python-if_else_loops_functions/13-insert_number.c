#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list
 *
 * @head: a pointer of pointer
 * @number: input number
 *
 * Return: a new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *n_node = malloc(sizeof(listint_t));

	if (n_node == NULL)
		return (NULL);
	n_node->n = number;

	if (node == NULL || node->n >= number)
	{
		n_node->next = node;
		*head = n_node;
		return (n_node);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	n_node->next = node->next;
	node->next = n_node;

	return (n_node);
}
