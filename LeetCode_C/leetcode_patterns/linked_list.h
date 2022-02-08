/*****************************************************************************
 * Linked List - Header
 *
 * nlantau, 2022-02-07
 ****************************************************************************/

#ifndef LINKED_LIST_H_
#define LINKED_LIST_H_

/**** Includes **************************************************************/
#include <stdlib.h>
#include <stdio.h>

/**** Prototypes ************************************************************/
struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode *make_node(int value);
void insert_node(struct ListNode *head, int val);
void push_node(struct ListNode **head, int val);
void print_list(struct ListNode *head);
int free_list(struct ListNode *head);

/****************************************************************************/
#endif /* LINKED_LIST_H_ */
