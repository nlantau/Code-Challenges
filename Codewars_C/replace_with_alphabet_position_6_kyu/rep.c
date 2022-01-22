/* Replace with alphabet position - 6 kyu
 * nlantau, 2021-08-29
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int to_lower(char s)
{
	if (96 < s && s < 123) return s - 96;
	if (64 < s && s < 91 ) return s + 32 - 96;
	return 0;
}

char *alphabet_position(const char *t)
{
	int len = strlen(t), i = 0;
	int *v = malloc(sizeof(int) * len * 4), *vv;
	char *s = malloc(sizeof(int) * len * 4), buf[5];

	for (; i < len; ++i) v[i] = to_lower(*t++);
	vv = v;
	for (i = 0; i < len; i++) {
		if (v[i] == 0)
			continue;
		snprintf(buf, 5, "%d ", v[i]);
		strcat(s, buf);
	}
	s[strlen(s) - 1] = '\0';
	v = vv;
	free(v);
	v = NULL;

	return s;
}

int main(void)
{
	char *a = "The sunset sets at twelve o' clock.";
	char *s = alphabet_position("The sunset sets at twelve o' clock.");

	printf("%s =\n ", a);
	printf("\"%s\"\n", s);

	free(s);
	s = NULL;
	return 0;
}

