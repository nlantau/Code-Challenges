/*****************************************************************************
 * LeetCode Patterns - Middle of the Linked List
 *
 * nlantau, 2022-02-06
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**** Strategy ***************************************************************
 * 1. Get size of linked list
 * 2. Move head to half the size
 * 3. Return head
 *
 ****************************************************************************/

struct ListNode {
    int val;
    struct ListNode *next;
};

int sizeof_list(struct ListNode *head)
{
	if(head == NULL)
		return 0;
	struct ListNode *curr = head;
	int counter = 0;
	while(curr != NULL) {
		counter++;
		curr = curr->next;
	}
	return counter;
}

struct ListNode* middleNode(struct ListNode* head)
{
	struct ListNode *curr = head;
	int size = sizeof_list(head);
	size /= 2;
	while(size > 0) {
		curr = curr->next;
		size--;
	}
	head = curr;
	return head;
}

void print_list(struct ListNode *head)
{
	struct ListNode *curr = head;

	while(curr != NULL) {
		printf("%d,", curr->val);
		curr = curr->next;
	}
}

/**** Notes ******************************************************************
 * 4 ms, 14.56% faster, 5.8 MB, 55.92% better
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

	a->val = 1;
	b->val = 2;
	c->val = 3;
	d->val = 4;
	e->val = 5;

	a->next = b;
	b->next = c;
	c->next = d;
	d->next = e;
	e->next = NULL;

	print_list(a);
	printf("\n\n> SEP <\n\n");

	struct ListNode *t = middleNode(a);
	print_list(t);
	printf("\n\n> SEP <\n\n");


	free(a); a = NULL;
	free(b); b = NULL;
	free(c); c = NULL;
	free(d); d = NULL;
	free(e); e = NULL;

	/* Example 2 */
	struct ListNode *a2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *b2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *c2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *d2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *e2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *f2 = (struct ListNode*)malloc(sizeof(struct ListNode));

	a2->val = 1;
	b2->val = 2;
	c2->val = 3;
	d2->val = 4;
	e2->val = 5;
	f2->val = 6;

	a2->next = b2;
	b2->next = c2;
	c2->next = d2;
	d2->next = e2;
	e2->next = f2;
	f2->next = NULL;

	print_list(a2);
	printf("\n\n> SEP <\n\n");

	struct ListNode *t2 = middleNode(a2);
	print_list(t2);
	printf("\n\n> SEP <\n\n");


	free(a2); a2 = NULL;
	free(b2); b2 = NULL;
	free(c2); c2 = NULL;
	free(d2); d2 = NULL;
	free(e2); e2 = NULL;

	/* Example 3 */

	return 0;
}
