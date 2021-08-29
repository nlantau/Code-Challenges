/* Printer Errors - 7 kyu
 * nlantau, 2021-08-30
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int errors(char s)
{
	if (s < 97 || 109 < s) return 1;
	return 0;
}

char *printerError(char *s)
{
	int len = strlen(s), errs = 0;
	char *a = malloc(sizeof(char) * len);
	while (*s != '\0')
		errs += errors(*s++);
	sprintf(a, "%d/%d", errs, len);
	return a;
}

int main(void)
{
	char *s = printerError("aaabbbbhaijjjm");
	printf("%s\n", s);
	free(s);
	s = NULL;

	char *a = printerError("aaaxbbbbyyhwawiwjjjwwm");
	printf("%s\n", a);

	free(a);
	a = NULL;

	return 0;
}

