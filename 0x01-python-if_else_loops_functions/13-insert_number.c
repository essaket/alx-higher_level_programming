#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - a function that inserts a number into a sorted singly linked list
 *
 * @head: input pointer of pointer
 * @number: input number
 *
 * Return: insert node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *n_node = malloc(sizeof(listint_t));

	if (!n_node)
		return (NULL);
	n_node->n = number;
	n_node = NULL;

	if (!node || n_node->n < node->n)
	{
		n_node->next = node;
		return (*head = n_node);
	}
	while (node)
	{
		if (!node->next || n_node->n < node->next->n)
		{
			n_node->next = node->next;
			n_node->next = n_node;
			return (n_node);
		}
		node = node->next;
	}
	return (NULL);
}
