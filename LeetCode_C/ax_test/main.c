/*****************************************************************************
 * Task 1 - Mattias test
 *
 * nlantau, 2022-03-13
 * start: 13:50
 * end  : 14:45
 ****************************************************************************/

/**** Includes **************************************************************/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <limits.h>
#include <assert.h>

/**** Defines ***************************************************************/
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

/**** Typedefs **************************************************************/
/**** Defines ***************************************************************/
/**** Variables *************************************************************/
/**** Constants *************************************************************/
/**** Prototypes ************************************************************/
char *solution(int T[], int N);

/**** Functions *************************************************************/
int main(void)
{
    /* Test 1 */
    int a[] = {-3,-14,-5,7,8,42,8,3};                     //< 34 -> SUMMER
    char *res_a = solution(a, (sizeof(a)/sizeof(a[0])));

    assert(strcmp(res_a, "SUMMER") == 0);
    printf("> [%s]\n", res_a);

    free(res_a); res_a = NULL;


    /* Test 2 */
    int b[] = {2,-3,3,1,10,8,2,5,13,-5,3,-18};            //< 21 -> AUTUMN
    char *res_b = solution(b, (sizeof(b)/sizeof(b[0])));

    assert(strcmp(res_b, "AUTUMN") == 0);
    printf("> [%s]\n", res_b);

    free(res_b); res_b = NULL;

	return 0;
}

char *solution(int T[], int N)
{
    /* Assume that:
     * N % 4 == 0
     * -1000 <= T[i] <= 1000
     * 8 <= N <= 200
     *
     * Amplitude: abs(max(T_period_x), min(T_period_x))
     */
    if (N % 4 != 0) return NULL;

    char *periods[] = {
        "WINTER",
        "SPRING",
        "SUMMER",
        "AUTUMN",
    };

    int i = 0, j = 0;

    int period_size = N / 4, period_nr = 0;
    int temp_min = INT_MAX, temp_max = INT_MIN;
    int max_amp = 0, int diff = 0;

    char *s = malloc(sizeof(char) * 8);

    /* Nested loop, but only for readability. It's still O(N) */
    for (; i < N - 1; i += j, period_nr++) {
        for(j = 0; j < period_size; ++j) {
            temp_min = MIN(temp_min, T[i+j]);
            temp_max = MAX(temp_max, T[i+j]);
        }

        diff = temp_max - temp_min;
        diff = abs(diff);

        if (diff > max_amp)
            strcpy(s, periods[period_nr]);

        max_amp = MAX(max_amp, diff);
        temp_min = INT_MAX;
        temp_max = INT_MIN;
    }

    return s;

}
/**** End *******************************************************************/
