#include "lists.h"
/**
 * check_cycle - checks if it does loop or no
 * @list: list
 *
 * Return: 0 if cycle, 1 if not
*/
int check_cycle(listint_t *list)
{
	listint_t *travel1 = list;
	listint_t *travel2 = list;

	if (list == NULL)
		return (0);

	while (travel1 && travel2 && travel2->travel1)
	{
		travel1 = travel1->next;
		travel2 = travel2->next->next;

		if (travel1 == travel2)
			return (1);
	}
	return (0);
}
