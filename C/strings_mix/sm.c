/* Strings mix - 4 kyu
 * nlantau, 2021-09-13
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	char chr;
	int dig;
}cfreq;

char* mix(char* s1, char* s2);
void print_struct(cfreq *s);

int main(void)
{
	char *s1 = "my&friend&Paul has heavy hats! &";
	char *s2 = "my friend John has many many friends &";


	s1 = "A aaaa bb c";


	char *s3 = mix(s1,s2);
	printf("-> [%s]\n", s3);

	free(s3); s3 = NULL;
	return 0;
}

char* mix(char* s1, char* s2)
{
	char *ps1 = s1, *ps2 = s2;
	cfreq ss1[26];
	for (int i = 0; i < 26; i++)
		ss1[i].dig = 0;

	for (char a = 'a', i = 0; a <= 'z'; a++, i++) {
		ss1[i].chr = a;
		while(*s1) {
			if (*s1++ == a) {
				printf("*s1 = [%c]\n", *s1);
				ss1[i].dig++; 
			}
		}
		s1 = ps1;
	}

	print_struct(ss1);


	return calloc(1,1);
}

void print_struct(cfreq *s)
{
	for (int i = 0; i < 26; i++)
		printf("ss1[%2d].chr = [%2c]\tss1[%2d].dig = [%2d]\n",\
				i, s[i].chr, i, s[i].dig);
}
