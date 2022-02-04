/*****************************************************************************
 * LeetCode Patterns - Contains Duplicate
 *
 * nlantau, 2022-02-05
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**** Strategy ***************************************************************
 * 1. Sort the list, O(NlogN)
 * 2. Iterate over list. If nums[i] == nums[i+1] return true, else false
 *
 ****************************************************************************/

int cmpfunc(const void* a, const void* b)
{
	return ( *(int* )a - *(int* )b );
}

bool containsDuplicate(int* nums, int numsSize)
{
	qsort(nums, numsSize, sizeof(int), cmpfunc);
	int l = -1, r = numsSize - 1;

	while (++l < r)
		if(nums[l] == nums[l + 1])
			return true;
	return false;
}

/**** Notes ******************************************************************
 * 167 ms, 53.48% faster, 12.7MB, 45.50% better
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	int nums[4] = {1,2,3,1};
	int numsSize = sizeof(nums) / sizeof(int);
	bool ans = containsDuplicate(nums, numsSize);
	assert(ans == true);
	fputs(ans ? "true\n" : "false\n", stdout);

	/* Example 2 */
	int nums2[4] = {1,2,3,4};
	int numsSize2 = sizeof(nums2) / sizeof(int);
	bool ans2 = containsDuplicate(nums2, numsSize2);
	assert(ans2 == false);
	fputs(ans2 ? "true\n" : "false\n", stdout);

	/* Example 3 */
	int nums3[10] = {1,1,1,3,3,4,3,2,4,2};
	int numsSize3 = sizeof(nums3) / sizeof(int);
	bool ans3 = containsDuplicate(nums3, numsSize3);
	assert(ans3 == true);
	fputs(ans3 ? "true\n" : "false\n", stdout);

	return 0;
}
