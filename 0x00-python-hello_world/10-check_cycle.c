#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - a function that check a list fi cycle or not
 *
 * @list: a pinter of list
 *
 * Return: 1 if list is cycle or 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
