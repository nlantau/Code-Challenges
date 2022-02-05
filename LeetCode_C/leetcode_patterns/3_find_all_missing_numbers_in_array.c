/*****************************************************************************
 * LeetCode Patterns - Find All Number Disappeared in an Array
 *
 * nlantau, 2022-02-05
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

/**** Strategy ***************************************************************
 * Range is [1, n] - Don't forget about this
 * Brute force:
 * 1. Sort array, O(NlogN)
 * 2. Iterate over array
 *    if i != nums[i], add i to res array
 * 3. Return res array
 *
 * O(N):
 * 1. Given nums = [4,3,2,7,8,2,3,1] with no constrains on modifying nums,
 *    we use each element to inverse the value of element at chosen index.
 *    Example: i == 0, nums[nums[i]-1] == nums[4-1] == 7 set nums[3] = -7.
 *    This way, each value in nums will be used as an index for nums. The 
 *    missing values will therefore lead to nums having indexes not having
 *    their values inversed. The indexes of theses not-inversed values should
 *    be appended to a new array that in the end should be returned.
 ****************************************************************************/
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void print_arr(int* nums, int numsSize)
{
	int j = 0;
	printf("[");
	while (j < numsSize) printf("%d,", nums[j++]);
	printf("]\n");
}

int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize)
{
	for (int i = 0; i < numsSize; ++i)
		nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1]);
	print_arr(nums, numsSize);

	int *res = malloc((*returnSize = 0) * sizeof(int));
	for (int i = 0; i < numsSize; ++i)
		if(nums[i] > 0) {
			res = realloc(res, ++(*returnSize) * sizeof(int));
			res[*returnSize - 1] = i + 1;
		}
	print_arr(res, *returnSize);
	return res;
}

/**** Notes ******************************************************************
 * 920 ms, 5.21% faster, 764.9 MB, 5.20% better
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	int nums[8] = {4,3,2,7,8,2,3,1};
	int retSize = 2;
	int *res = findDisappearedNumbers(nums, 8, &retSize);
	free(res); res = NULL;

	/* Example 2 */
	int nums2[2] = {1,1};
	int retSize2 = 1;
	int *res2 = findDisappearedNumbers(nums2, 2, &retSize2);
	free(res2); res2 = NULL;

	/* Example 3 */

	return 0;
}
