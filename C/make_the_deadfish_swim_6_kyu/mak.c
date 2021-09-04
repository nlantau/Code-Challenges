/* Make the Deadfish swim - 6 kyu
 * nlantau, 2021-09-04
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *parse(char *s)
{
	int *i = calloc(strlen(s), sizeof(int)), *r;
	r = i;
	*i = 0;

	while (*s) {
		if (*s == 'i') (*i)++;
		else if (*s == 's') *i *= (*i);
		else if (*s == 'd') (*i)--;
		else if (*s == 'o') {
			*i++;
			*i = *(i-1);
		}
		*s++;
	}
	i = r;
	return i;
}

int main(void)
{
	int *i = parse("iiisdoso"), *si;
	//printf("i-address: %x\n", i);

	si = i;
	while (*i)
		printf("i=%d\n", *i++);
	//printf("i-address: %x\n", i);
	i = si;
	//printf("i-address: %x\n", i);

	free(i);
	i = NULL;

	return 0;
}
