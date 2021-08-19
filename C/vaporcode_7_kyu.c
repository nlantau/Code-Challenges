/* nlantau, 2021-08-19
 * V A P O R C O D E
 *
 * Vaporwave: Converts sentence into all uppercase,
 *            and adds 2 spaces between each letter
 *            (or special character)
 *
 * Not Completed. Off-by-one error somewhere...
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void vaporcode(const char *src, char *dst)
{
	int i;
	char c;
	
	for (i = 0; i < strlen(src); i++) {
		c = src[i];
		if (c > 96 && c < 123)
			dst[i] = c - 32;
		else
			dst[i] = c;
	}
	printf("> 1st dst: %s.\n", dst);

	int j;
	char *d = (char *)malloc(strlen(dst) + 1);
	
	//char d[strlen(dst) + 1];
	printf("d size   : %ld\n", strlen(d));

	for (i = 0, j = 0; i < strlen(dst); i++, j++) {

		if (dst[i] != 32) {
			d[j] = dst[i];
			if (i != strlen(src) - 1) {
				if (dst[i+1] != 32) {
					d[j+1] = 32;
					d[j+2] = 32;
					j++;
					j++;
				} else {
					d[j+1] = 32;
					j++;
				}
			}
		}
		else
			d[j] = dst[i];

	}
	snprintf(dst, strlen(d) + 1, "%s", d);
	printf("d        : %s.\n", d);
	printf("> 2nd dst: %s.\n", dst);
	printf("> dst end: %c.\n", dst[strlen(dst)-1]);
	free(d);
	d = NULL;

}

int main(void) 
{
	const char a[] = "Let's go to the movies";
	const char x[] = "Why isn't my code working?";
	char b[53];
	char y[65];

	vaporcode(a, b);
	printf("> main()b: %s.\n", b);

	vaporcode(x, y);
	printf("> main()y: %s.\n", y);

	return 0;
}
