/* Strings mix - 4 kyu
 * nlantau, 2021-09-13
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
	char nos;
	char chr;
	int dig;
	int len;
} c_table;

char* mix(char* s1, char* s2);
void print_struct(c_table *s, c_table *t);
void print_ctable(c_table **s);

int main(void)
{
	char *s1 = "my&friend&Paul has heavy hats! &";
	char *s2 = "my friend John has many many friends &";
	//char *s4 = "A aaaa bb c";

	char *s3 = mix(s1,s2);
	printf("main -> [%s]\n", s3);
	free(s3); s3 = NULL;

	return 0;
}

char* mix(char* s1, char* s2)
{
	char *ps1 = s1, *ps2 = s2;
	c_table ss1[26], ss2[26];
	// Set dig to start value: 1
	for (int i = 0; i < 26; i++) {
		ss1[i].dig = 0;
		ss2[i].dig = 0;
	}
	// Count frequency
	for (char a = 'a', i = 0; a <= 'z'; a++, i++) {
		ss1[i].chr = a;
		ss2[i].chr = a;
		while(*s1) if (*s1++ == a) ss1[i].dig++;
		while(*s2) if (*s2++ == a) ss2[i].dig++;
		s1 = ps1;
		s2 = ps2;
	}
	print_struct(ss1, ss2);
	
	int k = 0, ts = 2;
	int s1ctc = 0, s2ctc = 0;
	c_table **f = NULL;
	int fc = 0, fs = 2;

	for (int i = 0; i < 26; i++) {

		// Only 'strictly greater than 1 is interesting
		if (ss1[i].dig > 1 || ss2[i].dig > 1) {
			s1ctc = 0, s2ctc = 0;

			for (int j = 0; j < ss1[i].dig; j++) s1ctc++;
			for (int j = 0; j < ss2[i].dig; j++) s2ctc++;

			if (s1ctc > s2ctc) {
				f = realloc(f, ++fs * sizeof(c_table*));
				f[fc] = calloc(1, sizeof(c_table));
				f[fc]->nos = '1';
				f[fc]->chr = ss1[i].chr;
				f[fc]->dig = 0;
				f[fc++]->len = s1ctc;
			} else if (s1ctc < s2ctc) {
				f = realloc(f, ++fs * sizeof(c_table*));
				f[fc] = calloc(1, sizeof(c_table));
				f[fc]->nos = '2';
				f[fc]->chr = ss2[i].chr;
				f[fc]->dig = 0;
				f[fc++]->len = s2ctc;
			} else if (s1ctc == s2ctc) {
				f = realloc(f, ++fs * sizeof(c_table*));
				f[fc] = calloc(1, sizeof(c_table));
				f[fc]->nos = '=';
				f[fc]->chr = ss2[i].chr;
				f[fc]->dig = 0;
				f[fc++]->len = s2ctc;
			}
		}
	}

	print_ctable(f);
	printf("Here\n");

	for (int i = 0; f[i] != '\0'; i++)
		free(f[i]);
	free(f); f = NULL;

	return calloc(1,1);
}


void print_ctable(c_table **s)
{
	for (int i = 0; s[i] != '\0'; i++) {
		printf("c_o[%2d].nos = |%2c|->| c_o[%2d]."
		       "chr = |%2c|->| c_o[%2d].len = |%2d|\n", 
		       i, s[i]->nos,
		       i, s[i]->chr, i, s[i]->len);
	}
}

void print_struct(c_table *s, c_table *t)
{
	for (int i = 0; i < 26; i++)
		printf("ss1[%2d].chr = [%2c]->ss1[%2d].dig = [%2d] | "
		       "ss2[%2d].chr = [%2c]->ss2[%2d].dig = [%2d]\n",
		       i, s[i].chr, i, s[i].dig,
		       i, t[i].chr, i, t[i].dig);
}
