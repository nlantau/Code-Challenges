/*****************************************************************************
 * LeetCode Patterns - Palindrome Linked List
 *
 * nlantau, 2022-02-06
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MEMORYKILLER 0

/**** Strategy ***************************************************************
 * The Strategic Way
 * 1. Put curr->val in array. Keep track of length.
 * 2. If length % 2, return false 
 * 3. if arr[i] != arr[length - 1 -i], return false
 * 4. return true
 ****************************************************************************/
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode* reverse(struct ListNode *head)
{
	/*
	 * Learn this pattern by heart!
	 */
	struct ListNode *next = NULL, *prev = NULL;

	while(head != NULL) {
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}
	return prev;
}

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

#if MEMORYKILLER
bool isPalindrome(struct ListNode* head)
{
	/* This works, but not for large N. */
	int size, i = 0;
	int *arr = (int*)malloc((size = 0) * sizeof(int));
	struct ListNode *curr = head;
	
	while(curr != NULL) {
		arr = realloc(arr, ++size * sizeof(int));
		arr[size - 1] = curr->val;
		curr = curr->next;
	}
	if(size == 1) return true;

	while(i < (size/2)) {
		if(arr[i] != arr[size - 1 - i]) {
			free(arr);
			return 0;
		}
		i++;
	}
	free(arr);
	return 1;
}

#else

/**** Strategy ***************************************************************
 * Reversing the list
 * 1. Use slow and fast pointers to get to the 50% and 100% of list at once
 * 2. Reverse from slow->next to end of list
 *    This way head will point at beginning of list and we'll have
 *    a reversed list pointing at the starting from the end of the original
 *    list
 * 3. Then simply iterate over both lists (curr = curr->next, rev = rev->next)
 *    while checking if their values are equal or not. 
 ****************************************************************************/


bool isPalindrome(struct ListNode* head)
{
	struct ListNode *slow = head, *fast = head;
	while(fast->next != NULL && fast->next->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
	}
	struct ListNode *rev = reverse(slow->next);
	slow->next = NULL;

	while(head != NULL && rev != NULL) {
		if(head->val != rev->val)
			return 0;
		head = head->next;
		rev  = rev->next;
	}

	return 1;
}
#endif

/**** Notes ******************************************************************
 * 243 ms, 25.86% faster, 41.4 MB, 65.91% better
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	struct ListNode *a = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *b = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *c = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *d = (struct ListNode*)malloc(sizeof(struct ListNode));

	a->val = 1;
	b->val = 2;
	c->val = 2;
	d->val = 1;

	a->next = b;
	b->next = c;
	c->next = d;
	d->next = NULL;

	print_list(a);
	bool res = isPalindrome(a);
	assert(res == true);
	struct ListNode *aa = reverse(a);

	print_list(aa);

	free(a); a = NULL;
	free(b); b = NULL;
	free(c); c = NULL;
	free(d); d = NULL;

	/* Example 2 */
	struct ListNode *a1 = (struct ListNode*)malloc(sizeof(struct ListNode));
	struct ListNode *b1 = (struct ListNode*)malloc(sizeof(struct ListNode));

	a1->val = 1;
	b1->val = 2;

	a1->next = b1;

	print_list(a1);
	bool res1 = isPalindrome(a1);
	assert(res1 == false);

	print_list(a1);

	free(a1); a1 = NULL;
	free(b1); b1 = NULL;
	/* Example 3 */

	return 0;
}
