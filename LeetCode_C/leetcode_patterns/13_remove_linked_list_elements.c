/*****************************************************************************
 * LeetCode Patterns - Remove Linked List Elements
 *
 * nlantau, 2022-02-06
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**** Strategy ***************************************************************
 * 1. Iterate while curr->next != NULL
 * 2. if curr->next->val == val, remove node by setting 
 *    curr->next to curr->next->next, otherwise move one
 *    node by setting curr = curr->next
 * 3. Final check of head: If head->val == val, move
 *    pointer to head->next
 * 4. return head
 *
 ****************************************************************************/

struct ListNode {
    int val;
    struct ListNode *next;
};

void print_list(struct ListNode *head)
{
	struct ListNode *curr = head;

	printf("[");
	while(curr != NULL) {
		printf("%d,", curr->val);
		curr = curr->next;
	}
	printf("]\n");
}

struct ListNode* removeElements(struct ListNode *head, int val)
{
	if (head == NULL)
		return head;

	struct ListNode *curr = head;

	while (curr->next != NULL) {
		if (curr->next->val == val) 
			curr->next = curr->next->next;
		else
			curr = curr->next;
	}
	if (head->val == val)
		head = head->next;
	return head;
}

/**** Notes ******************************************************************
 * 26 ms, 18.30% faster, 8 MB, 55.33% better
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	struct ListNode *a = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *b = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *c = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *d = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *e = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *f = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *g = (struct ListNode*)malloc(sizeof(struct ListNode));

	a->val = 1;
	b->val = 2;
	c->val = 6;
	d->val = 3;
	e->val = 4;
	f->val = 5;
	g->val = 6;

	a->next = b;
	b->next = c;
	c->next = d;
	d->next = e;
	e->next = f;
	f->next = g;
	g->next = NULL;

	print_list(a);
	a = removeElements(a, 6);
	print_list(a);

	//assert(res == true);


	free(a); a = NULL;
	free(b); b = NULL;
	free(c); c = NULL;
	free(d); d = NULL;
	free(e); e = NULL;
	free(f); f = NULL;

	/* Example 2 */

	/* Example 3 */

	return 0;
}
