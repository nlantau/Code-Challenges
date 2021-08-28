/* Isograms - 7 kyu
 * nlantau, 2021-08-29
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


char to_lower(char a)
{
	if (96 < a && a < 123) return a;
	return a + 32;
}


bool IsIsogram(char *s)
{
	int len = strlen(s), i = 0;
	char *a = malloc(sizeof(char) * len);

	for (; i < len + 1; ++i) a[i] = to_lower(*s++);

	for (int x = 0; x < len; ++x)
		for (int y = 0; y < len; ++y) {
			if (x == y)
				continue;
			if (a[x] == a[y])
				return false;
		}

	free(a);
	return true;
}


int main(void)
{
	//printf("to_lower: %c\n", to_lower('a'));
	//printf("to_lower: %c\n", to_lower('A'));
	
	printf("true : %s\n", IsIsogram("Dermatoglyphics") ? "true" : "false");
	printf("false: %s\n", IsIsogram("aba") ? "true" : "false");
	printf("false: %s\n", IsIsogram("moOse") ? "true" : "false");
	return 0;
}
