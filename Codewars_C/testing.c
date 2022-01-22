/* Testing - testing various methods spotted
 *           in different kata solutions
 * nlantau, 2021-08-29
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>





char *accum(const char *s)
{
	int len = strlen(s);
	printf("len = %d\n", len);

	int k = 0;
	for (; k < len + 1; ++k)
		printf("!k: %d\n", !k), printf("k : %d\n", k);

	return "1337";
}



int main(void)
{
	char *s = "abcd";
	char *a = accum(s);
	printf("a: %s\n", a);

	return 0;
}
