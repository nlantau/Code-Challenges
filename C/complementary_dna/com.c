/* Complementary DNA - 7 kyu
 * nlantau, 2021-08-29
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void append(char *s, char c)
{
	size_t len = strlen(s);
	s[len] = c;
	s[len + 1] = '\0';
}

char trans(char a)
{
	if (a == 65) return 84;
	if (a == 84) return 65;
	if (a == 67) return 71;
	if (a == 71) return 67;
	return 32;
}

char *dna_strand(const char *dna)
{
	int len = strlen(dna), i = 0;
	size_t rs = 1;
	char *s = malloc(sizeof(char));

	for (; i < len; ++i) {
		s = realloc(s, ++rs * sizeof(char));
		append(s, trans(dna[i]));
	}

	return s;
}

char *stolen(const char *dna)
{
	char *result = strdup(dna);
	char *cp = result;
	while(*cp != '\0') {
		switch (*cp) {
			case 'A': *cp = 'T'; break;
			case 'C': *cp = 'G'; break;
			case 'G': *cp = 'C'; break;
			case 'T': *cp = 'A'; break;
		}
		cp++;
	}
	return result;
}

static const char dna_compl_map[] = {
	['A'] = 'T',
	['T'] = 'A',
	['C'] = 'G',
	['G'] = 'C'
};

char *stolen_2(const char *dna)
{
	int len = strlen(dna);
	char *ret_string = malloc(len * sizeof(char) + 1);
	memset(ret_string, 0, len * sizeof(char) + 1);

	for (int i = 0; i < len; i++)
		ret_string[i] = dna_compl_map[dna[i]];
	return ret_string;
}

int main(void)
{
	char *s = "GTAT";
	char *a = dna_strand(s);
	printf("\"%s\"\n", a);

	printf("->%s\n", stolen(s));
	printf("->%s\n", stolen_2(s));

	free(a);
	a = NULL;
	return 0;
}
