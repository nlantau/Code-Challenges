/*****************************************************************************
 * LeetCode Patterns - Missing Number
 *
 * nlantau, 2022-02-05
 ****************************************************************************/
#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**** Strategy ***************************************************************
 * 1. Given length of array, we could sum the series of natural numbers, 
 *    subtract the sum of nums and we should get our result. Keep in mind,
 *    the series starts at zero and not 1! [0, n]
 *
 ****************************************************************************/

int missingNumber(int* nums, int numsSize){
	int nums_sum = 0, series_sum = 0;

	for(int i = 0; i < numsSize+1; ++i) {
		series_sum += i;
		if (i < numsSize)
			nums_sum += nums[i];
	}
	return series_sum - nums_sum;
}


/**** Notes ******************************************************************
 * 24 ms, 51.42% faster, 6.5 MB, 63.65% better
 *
 ****************************************************************************/

int main(void)
{
	/* Example 1 */
	int nums1[3] = {3,0,1};
	int numsSize1 = sizeof(nums1) / sizeof(int);
	int ans1 = missingNumber(nums1, numsSize1);
	assert(ans1 == 2);
	printf("%d\n", ans1);

	/* Example 2 */
	int nums2[2] = {0,1};
	int numsSize2 = sizeof(nums2) / sizeof(int);
	int ans2 = missingNumber(nums2, numsSize2);
	assert(ans2 == 2);
	printf("%d\n", ans2);

	/* Example 3 */
	int nums3[9] = {9,6,4,2,3,5,7,0,1};
	int numsSize3 = sizeof(nums3) / sizeof(int);
	int ans3 = missingNumber(nums3, numsSize3);
	assert(ans3 == 8);
	printf("%d\n", ans3);

	return 0;
}
