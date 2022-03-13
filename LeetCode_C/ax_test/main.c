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
#include <signal.h>

/**** Defines ***************************************************************/
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

/**** Typedefs **************************************************************/
enum _period {
    winter, spring, summer, autumn,
};

static const char *period[] = {
    "WINTER", "SPRING", "SUMMER", "AUTUMN",
};

/**** Variables *************************************************************/
/**** Constants *************************************************************/
/**** Prototypes ************************************************************/
char *solution(int T[], int N);
void sig_handler(int signum);

/**** Functions *************************************************************/
int main(int argc, char *argv[])
{
    signal(SIGABRT, sig_handler);

    int *a, size;

    /* Test 1 - Either pass int arr as argv or run default */
    if (argc > 1) {
        size = argc - 1;
        a = malloc(sizeof(int) * size);

        for (int x = 0; x < size; ++x)
            sscanf(argv[x + 1], "%d", &a[x]);

    } else if (argc == 1) {
        int x[] = {-3,-14,-5,7,8,42,8,3};                     //< 34 -> SUMMER
        size = sizeof(x)/sizeof(x[0]);

        a = malloc(sizeof(int) * size);
        memcpy(a, x, size*sizeof(*a));
    }

    char *res_a = solution(a, size);

    free(a); a = NULL;

    if (argc == 1)
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

void sig_handler(int signum)
{
    printf("> Oh well... Caught signal %d..\n", signum);
    exit(1);
}

char *solution(int T[], int N)
{
    /* 8 <= N <= 200
     * -1000 <= T[i] <= 1000
     */
    if (N % 4 != 0) return NULL;

    char *s = malloc(sizeof(char) * 8);
    int temp_min = INT_MAX, temp_max = INT_MIN, max_amp = 0, diff = 0;

    /* Nested loop, but it's still O(N) */
    for (int i = 0, j = 0, period_size = N / 4, period_nr = 0; i < N - 1; i += j, period_nr++) {
        for(j = 0; j < period_size; ++j) {
            temp_min = MIN(temp_min, T[i+j]);
            temp_max = MAX(temp_max, T[i+j]);
        }

        if ((diff = abs(temp_max - temp_min)) > max_amp)
            strcpy(s, period[period_nr]);

        max_amp = MAX(max_amp, diff);
        temp_min = INT_MAX;
        temp_max = INT_MIN;
    }
    return s;
}
/**** End *******************************************************************/
