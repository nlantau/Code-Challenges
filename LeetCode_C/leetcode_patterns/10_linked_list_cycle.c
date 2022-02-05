/*****************************************************************************
 * LeetCode Patterns - Linked List Cycle
 *
 * nlantau, 2022-02-05
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**** Strategy ***************************************************************
 * 1. Slow & Fast pointers. If s == f return true, else false
 *
 ****************************************************************************/

// Definition for singly-linked list.
struct ListNode {
	int val;
	struct ListNode *next;
};

bool hasCycle(struct ListNode *head)
{
	if (head == NULL)
		return false;
	struct ListNode *slow = head;
	struct ListNode *fast = head->next;

	while(slow != fast) {
		if(fast == NULL || fast->next == NULL)
			return false;
		slow = slow->next;
		fast = fast->next->next;
	}
	return true;
}

/**** Notes ******************************************************************
 * 17 ms, 34.53% faster, 7.9MB, 44.97% better
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	struct ListNode *a = NULL;
	struct ListNode *b = NULL;
	struct ListNode *c = NULL;
	struct ListNode *d = NULL;

	a = (struct ListNode*)malloc(sizeof(struct ListNode));
	b = (struct ListNode*)malloc(sizeof(struct ListNode));
	c = (struct ListNode*)malloc(sizeof(struct ListNode));
	d = (struct ListNode*)malloc(sizeof(struct ListNode));

	a->val = 3;
	a->next = b;
	b->val = 2;
	b->next = c;
	c->val = 0;
	c->next = d;
	d->val = -4;
	d->next = b;

	bool res = hasCycle(a);
	free(a); a = NULL;
	free(b); b = NULL;
	free(c); c = NULL;
	free(d); d = NULL;

	assert(res == true);

	/* Example 2 */
	struct ListNode *a1 = NULL;
	struct ListNode *b1 = NULL;
	a1 = (struct ListNode*)malloc(sizeof(struct ListNode));
	b1 = (struct ListNode*)malloc(sizeof(struct ListNode));

	a1->val = 1;
	a1->next = b1;
	b1->val = 2;
	b1->next = a;

	bool res1 = hasCycle(a1);

	free(a1); a1 = NULL;
	free(b1); b1 = NULL;

	assert(res1 == false);

	/* Example 3 */
	struct ListNode *a2 = (struct ListNode*)malloc(sizeof(struct ListNode));
	a2->val = 1;
	a2->next = NULL;

	bool res2 = hasCycle(a2);

	free(a2); a2 = NULL;

	assert(res2 == false);

	return 0;
}
