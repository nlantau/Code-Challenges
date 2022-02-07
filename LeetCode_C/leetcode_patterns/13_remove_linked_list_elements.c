/*****************************************************************************
 * LeetCode Patterns - Remove Linked List Elements
 *
 * nlantau, 2022-02-06
 ****************************************************************************/
#include "linked_list.h"
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
	struct ListNode *a = make_node(1);
	insert_node(a, 2);
	insert_node(a, 6);
	insert_node(a, 3);
	insert_node(a, 4);
	insert_node(a, 5);
	insert_node(a, 6);

	print_list(a);
	a = removeElements(a, 6);
	print_list(a);


	if (free_list(a))
		return 0;

	/* Example 2 */

	/* Example 3 */

	return -1;
}
