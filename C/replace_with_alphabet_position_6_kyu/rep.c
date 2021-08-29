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
	char *s = malloc(sizeof(char) * len * 4);
	char n[3];

	for (; i < len; ++i) {
		if (to_lower(*t) != 0) {
			//n[0] = 0,n[1] = 0,n[2] = 0;
			sprintf(n, "%d", to_lower(*t));
			for (int k = 0; n[k] != 0; ++k)
				s[i] = n[k];
		}
		*t++;
	}
	printf("s:%s.\n",s);

	free(s);
	s = NULL;

	return "Hej";
}


int main(void)
{
	//printf("%s.\n", alphabet_position("abcd"));
	//printf("%s.\n", alphabet_position("z bcd"));
	printf("%s.\n", alphabet_position("z"));

	return 0;
}

