/* Binaries - 6 kyu
 * nlantau, 2021-09-04
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *bin(char c)
{
	int i = 5, k;
	int first_one = 0;
	char *s = calloc(6, sizeof(char)), *t;
	char *x = calloc(6, sizeof(char)), *y;
	t = s;
	y = x;

	for (; i >= 0; i--, *s++) {
		k = c >> i;
		if (k & 1) *s = '1';
		else *s = '0';
	}
	*(s+1) = '\0';
	s = t;
	while (*s++ != '1') first_one++;
	*s--;
	*s--;
	while (*s++ != '\0')
		*x++ = *s;
	*(x+1) = '\0';
	x = y;
	s = t;
	free(s);
	s = NULL;
	return x;
}


char *code(const char *org)
{
	/* 
	 * for d in s:
	 * 	k = number of bits for d
	 * 	
	 *	# Stage 1
	 * 	if (k > 1)
	 * 		concat '0' (k-1) times, follwed by '1'
	 * 	else
	 * 		concat '1'
	 *
	 * 	# Stage 2
	 * 	convert d to binary string (LSB most right bit)
	 *
	 * 	# Stage 3
	 * 	concat stage 1 and stage 2
	 *
	 * concat all stage 3
	 *
	 */

	// Char * for stage 1,2 & 3
	char *s1 = calloc(50, sizeof(char)), *s1s;
	char *s2 = calloc(250, sizeof(char)), *s2s;
	char *bin_trim;
	char *orgs;
	
	// Save start pos
	s1s = s1;
	s2s = s2;
	orgs = org;

	int k = 0, t;

	for (; *org != '\0'; *org++) {
		// works for d > 1
		if (*org - 48 > 0) {
			bin_trim = bin(*org - 48);
			k = strlen(bin_trim);
			if (k > 1) {
				t = k - 1;
				while (t-- != 0) {
					*s1++ = '0';
				}
				*s1++ = '1';
				s1 = s1s;
				// s1 is good here
				sprintf(s1, "%s%s", s1, bin_trim);
			} else if (k == 1) {
				sprintf(s1, "%d%d", 1, 1);
			}

			free(bin_trim);
			bin_trim = NULL;
		} 
		// Should take care of d = 1 or 0
		else 
			sprintf(s1, "%d%d", 1, 0);
		sprintf(s2, "%s%s", s2, s1);
		s1 = s1s;
		memset(s1, '\0', 50);
	}

	// Restore starter pos
	s1 = s1s;
	s2 = s2s;
	org = orgs;

	// Free dynamic
	free(s1);
	s1 = NULL;

	return s2;
}

char *decode(const char *org)
{
	/*
	 * Given a binary string (encoded by code()),
	 * decode it to base 10.
	 *
	 * # Stage 1
	 * 1. Start from MSB.
	 * 2. Look at first digit
	 * 	a. if '1' -> Could be digit 0 or 1
	 * 	b. else 
	 * 		look at pos 1 and pos 2:
	 * 		if pos1 == 0 and pos2 == 1 -> Could be digit 2 or 3
	 * 		else if pos1 == 0 and pos2 == 0 -> Could be digit 4,5,6 or 7
	 * 			if not 4,5,6 ot 7
	 * 				look at pos3
	 * 				if pos3 == 0 -> either digit 8 or 9
	 * 					LSB == 0 -> digit 8
	 * 					LSB == 1 -> digit 9
	 *
	 * # Stage 2
	 * 1. Save the found/matching digit.
	 * 2. Trim down given string (remove binary part from stage 1)
	 * 3. Repeat stage 1 for next digit
	 *
	 * code(0) --> 10
	 * code(1) --> 11
	 * code(2) --> 0110
	 * code(3) --> 0111
	 * code(4) --> 001100
	 * code(5) --> 001101
	 * code(6) --> 001110
	 * code(7) --> 001111
	 * code(8) --> 00011000
	 * code(9) --> 00011001
	 *
	 */
	char *s = calloc(250, sizeof(char)), *sp;
	char *t = calloc(250, sizeof(char)), *tp, *orgp;

	sp = s;
	tp = s;
	orgp = org;
	
	int i = 0;
	int len = strlen(org);

	if (len < 1) return s;

	for (;*org != '\0';) {
		if (*org == 49) {
			*(org + 1) == 48 ? sprintf(s, "%c", 48) : sprintf(s, "%c", 49);
			*org++;
			*org++;
		} else {
			*org++;
		}
	}



	org = orgp;
	s = tp;
	free(t); t = NULL;
	return s;
}

int main(void)
{
	/*
	int i = 0;
	char s[4];
	for (; i < 10; i++) {
		sprintf(s, "%d", i);
		printf("code(%d) --> %s\n", i, code(s));
	}
	*/

	char *a = decode("10");
	printf("0:%s\n", a);
	free(a); a = NULL;

	char *b = decode("11");
	printf("1:%s\n", b);
	free(b); b = NULL;

	char *c = decode("0110");
	printf("2:%s\n", c);
	free(c); c = NULL;



	
	//printf("%s\n", code("77338855"));
	//printf("%s\n", code("77338"));
	//printf("%s\n", code("0011121314"));
	return 0;
}
