/* Detect Pangram - 6 kyu
 * nlantau, 2021-09-12
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

bool is_pangram(const char *);
int cmpfunc (const void *a, const void *b);

int main(void)
{
	char *s = "The quick, brown fox jumps over the lazy dog!"; // true
	printf("%s = [%s]\n",s, is_pangram(s) ? "true" : "false" );
	s = "The quick, brown fox jumped over the lazy dog!";
	printf("%s = [%s]\n",s, is_pangram(s) ? "true" : "false" );

	return 0;
}

int cmpfunc (const void *a, const void *b)
{
	return ( *(char*)a - *(char*)b);
}

bool is_pangram(const char *s)
{
	/*
	size_t i = strlen(s), j = 0, k = j;
	char *t = calloc(i+1, 1), *x = t;
	while (j != i) {
		if (isalpha(s[j]))
			*(t + k++) = tolower(s[j]);
		j++;
	}
	qsort(t, strlen(t), sizeof(char), cmpfunc);

	for (i = 0, j = 0; t[i] != '\0';)
		if (t[++i] != t[j] && i != ++j)
			t[j] = t[i];
	i = strlen(t);
	free(x); x = NULL;
	return i == 26 ? 1 : 0;
	*/
	for (char x = 'a'; x <= 'z'; x++)
		if (!strchr(s, x) && !strchr(s, x - 'a' + 'A'))
			return false;
	return true;
}


/*
 * Could've used strchr inside a for-loop:
 * for (char x = 'a'; x <= 'z'; x++) {
 * 	if (!strchr(str_in, x) && !strchr(str_in, x - 'a' + 'A'))
 * 		return false;
 * 	return true;
 *
 *
 */
