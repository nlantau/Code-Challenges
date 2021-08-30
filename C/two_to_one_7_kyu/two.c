/* Two to One - 7 kyu
 * nlantau, 2021-08-30
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void append(char *s, char c)
{
	size_t len = strlen(s);
	*(s+len) = c;
	*(s+len+1) = '\0';
}

int check_arr(char *s, char c)
{
	int i = 0, len = strlen(s);
	for (; i < len; i++) 
		if (c == *(s+i)) return 0;
	return 1;
}

void sort_(char *s)
{
	int len = strlen(s), i, j; 
	char t;

	for (i = 0; i < len - 1; i++)
		for (j = i + 1; j < len; j++)
			if (*(s+i) > *(s+j)) {
				t = *(s+i);
				*(s+i) = *(s+j);
				*(s+j) = t;
			}
}

char *longest(char *s1, char *s2)
{
	int len1 = strlen(s1), len2 = strlen(s2);
	int rp = 2;
	char *z = calloc(1, sizeof(char));
	char *j = calloc(len1 + len2, sizeof(char));
	int d = 0, p;

	sprintf(j, "%s%s", s1,s2);

	for (; d < len1 + len2; d++){
		p = check_arr(z, *(j+d));
		if (!p) continue;
		z = realloc(z, rp++ * sizeof(char));
		append(z, *(j+d));
	}
	sort_(z);
	free(j);
	j = NULL;
	return z;
}

int main(void)
{
	char *s = "xyaabbbccccdefww";
	char *t = "xxxxyyyyabklmopq";
	char *x = longest(s, t);
	printf("%s\n", x);
	free(x);
	x = NULL;

	s = "abcdefghijklmnopqrstuvwxyz";
	char *y = longest(s, s);
	printf("%s\n", y);
	free(y);
	y = NULL;

	char *as = "lordsofthefallen";
	char *st = "gamekult";
	char *c = longest(as, st);
	printf("%s\n", c);
	free(c);
	c = NULL;


	return 0;
}
