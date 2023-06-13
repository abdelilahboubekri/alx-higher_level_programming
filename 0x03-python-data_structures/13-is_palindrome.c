/*
 * File: 13-is_palindrome.c
 * Auth: Mbah Nkemdinma
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: it's pointer to the starting node of the list to reverse
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: it's pointer to the head of the linked list.
 *
 * Return: if the linked list is not a palindrome - 0.
 *         if the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *chg, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	chg = *head;
	while (chg)
	{
		size++;
		chg = chg->next;
	}

	chg = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		chg = chg->next;

	if ((size % 2) == 0 && chg->n != chg->next->n)
		return (0);

	chg = chg->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	chg = *head;
	while (rev)
	{
		if (chg->n != rev->n)
			return (0);
		chg = chg->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
