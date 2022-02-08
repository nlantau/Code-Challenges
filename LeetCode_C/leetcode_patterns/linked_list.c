/*****************************************************************************
 * Linked List - Source
 *
 * nlantau, 2022-02-07
 ****************************************************************************/

/**** Includes **************************************************************/
#include "linked_list.h"

#define TESTING 0

/**** Functions *************************************************************/
void print_list(struct ListNode *head)
{
	for (printf("["); head != NULL; head = head->next)
		printf("%d,", head->val);
	printf("]\n");
}

int free_list(struct ListNode *head)
{
	struct ListNode *prev = NULL;

	/* My most retarded for-statement ever */
	for (; head != NULL; printf("Freeing %d\n", prev->val), free(prev)) {
		prev = head;
		head = head->next;
		prev->next = NULL;
	}
	return 1;
}

void insert_node(struct ListNode *head, int val)
{
	struct ListNode *curr = head;
	struct ListNode *next = (struct ListNode*)malloc(sizeof(struct ListNode));
	next->val = val;
	next->next = NULL;

	for (; curr->next != NULL; curr = curr->next);

	curr->next = next;
}

void push_node(struct ListNode **head, int val)
{
	struct ListNode *new_head = (struct ListNode*)malloc(sizeof(struct ListNode));

	new_head->val = val;
	new_head->next = *head;
	*head = new_head;
}


struct ListNode *make_node(int value)
{
	struct ListNode *a = (struct ListNode*)malloc(sizeof(struct ListNode));
	a->val = value;
	a->next = NULL;
	return a;
}


/**** Testing ***************************************************************/
#if TESTING
int main(void)
{
	struct ListNode *a = make_node(1);
	print_list(a);
	insert_node(a, 2);
	print_list(a);
	insert_node(a, 3);
	print_list(a);

	if (free_list(a))
		return 0;

	return -1;
}
#endif /* TESTING */
/**** End *******************************************************************/
