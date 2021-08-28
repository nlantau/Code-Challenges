/* Mumbling - 7 kyu
 * nlantau, 2021-08-28
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int size(const char *ptr)
{
	int offset = 0, count = 0;
	while (*(ptr + offset) != '\0') {
		++count;
		++offset;
	}
	return count;
}


int fact(int len)
{
	int i, fact = 1;
	for (i = 1; i <= len; ++i)
		fact += i;
	return fact;
}


void append(char *s, char c)
{
	size_t len = strlen(s);
	s[len] = c;
	s[len + 1] = '\0';
}


char *accum(const char *s)
{
	int i = 0, j = 0, c = 0;
	size_t rs = 1;
	char x, *fs = malloc(sizeof(char));

	*fs = '\0';

	while (*(s + c) != '\0') {
		i++;
		for (j = 0; j < i; j++) {
			if (j == 0) {
				if (64 < *s && *s < 91)
					x = *s;
				else
					x = *s - 32;
				fs = realloc(fs, ++rs * sizeof(char));
				append(fs, x);
			} else {
				if (96 < *s && *s < 123)
					x = *s;
				else
					x = *s + 32;
				fs = realloc(fs, ++rs * sizeof(char));
				append(fs, x);
			}
		}
		*s++;
		if (*(s + c) != '\0') {
			fs = realloc(fs, ++rs * sizeof(char));
			append(fs, '-');
		}
	}
	return fs;
}


int main(void)
{
	char *fs = accum("RqaExty");
	printf("-> RqaExty = %s\n", fs);
	free(fs);
	fs = NULL;
	//printf("a: %c A: %c\n", 'a', ('a' & ~32));
	//printf("A: %c a: %c\n", 'A', ('A' | 32));

	return 0;
}
