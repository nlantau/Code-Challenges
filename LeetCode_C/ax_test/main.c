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
    int x[] = {-3,-14,-5,7,8,42,8,3};                     //< 34 -> SUMMER
                                                          //
    int *a = malloc(sizeof(int *)*8), i = 0;


    while (i < 8) {
        a[i] = x[i];
        i++;
    }

    printf("i: %d\n", i);

    char *res_a = solution(a, 8);

    free(a); a = NULL;

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
    if (N % 4 != 0) return NULL;

    char *periods[] = {"WINTER", "SPRING", "SUMMER","AUTUMN",}, *s = malloc(sizeof(char) * 8);
    int temp_min = INT_MAX, temp_max = INT_MIN, max_amp = 0, diff = 0;

    /* Nested loop, but it's still O(N) */
    for (int i = 0, j = 0, period_size = N / 4, period_nr = 0; i < N - 1; i += j, period_nr++) {
        for(j = 0; j < period_size; ++j) {
            temp_min = MIN(temp_min, T[i+j]);
            temp_max = MAX(temp_max, T[i+j]);
        }

        if ((diff = abs(temp_max - temp_min)) > max_amp)
            strcpy(s, periods[period_nr]);

        max_amp = MAX(max_amp, diff);
        temp_min = INT_MAX;
        temp_max = INT_MIN;
    }
    return s;
}
/**** End *******************************************************************/
