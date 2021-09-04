/* Remove the Parentheses - 6 kyu
 * nlantau, 2021-09-04
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void remove_parentheses(const char *si, char *so)
{
	int lc = 0;
	int rc = 0;

	while (*si != '\0') {
		if (*si == 40) {
			lc++;
			while (lc != rc || *si == 40 || *si == 41) {
				*si++;
				if (*si == 41)
					rc++;
				if (*si == 40)
					lc++;
			}
		}
		*so++ = *si++;
	}
	*so = '\0';
}

int main(void)
{
	char *s = "example (unwanted thing) example"; 
	char *t = calloc(strlen(s), sizeof(char));

	remove_parentheses(s,t);
	printf("%s -> %s\n", s,t);
	free(t);
	t = NULL;

	return 0;
}

