/*****************************************************************************
 * Playground - Pointers & References
 *
 * nlantau, 2022-02-07
 ****************************************************************************/
#include "linked_list.h"
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**** Functions *************************************************************/

void *reverse_list(void *head)
{
	/* Using void *, because why not...
	 * I had to play around a bit
	 */
	struct ListNode *curr = (struct ListNode*) head;
	struct ListNode *prev = NULL, *next = NULL;

	while (curr != NULL) {
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (void*) prev;
}

int dereference_void_pointer(void *a)
{
	/* Dereferencing a void pointer is not possible, which is
	 * why we need to typecast it to a type and then dereference
	 * that type
	 */
	printf("a = %d\n", *(int*)a);
	return 1;
}

void pointer_arithmetic(void)
{
	int arr[] = {1,1,2,2,3,4,4,5,1337};
	int size = sizeof(arr) / sizeof(int);

	printf("arr[0]: %d\n", *&arr[size - 1]);

	printf("arr[0]: %d\n", *&arr[0]);
	printf("arr[0]: %d\n", *arr);

	printf("arr[0]: %d\n", *&arr[sizeof(arr)/ sizeof(int)- sizeof(arr)/ sizeof(int)]);


	for (int i = 0; i < size; i++) {
		printf("%d,", *(arr + i));
		printf("%d,\n", arr[i]);
	}
		
	printf("\n");
}

/**** Notes ******************************************************************
 *
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	struct ListNode *a = make_node(1);
	insert_node(a, 2);
	insert_node(a, 3);
	insert_node(a, 4);
	insert_node(a, 5);
	print_list(a);
	a = (struct ListNode *) reverse_list(a);
	print_list(a);

	push_node(&a, 6);

	print_list(a);

	free_list(a);

	/* Example 2 */
	int b = 10;
	if (dereference_void_pointer(&b)) {
		pointer_arithmetic();
		return 0;
	}

	/* Example 3 */

	return -1;
}
