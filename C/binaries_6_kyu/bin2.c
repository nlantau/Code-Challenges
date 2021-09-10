/* Binaries - 6 kyu
 * nlantau, 2021-09-04
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *bin(char c)
{
	int i = 5, k;
	int first_one = 0;
	char *s = calloc(6, sizeof(char)), *t;
	char *x = calloc(6, sizeof(char)), *y;
	t = s;
	y = x;

	for (; i >= 0; i--, *s++) {
		k = c >> i;
		if (k & 1) *s = '1';
		else *s = '0';
	}
	*(s+1) = '\0';
	s = t;
	while (*s++ != '1') first_one++;
	*s--; *s--;
	while (*s++ != '\0')
		*x++ = *s;
	*(x+1) = '\0';
	x = y;
	s = t;
	free(s);
	s = NULL;
	return x;
}


char *code(const char *org)
{
	char *s1 = calloc(50, sizeof(char)), *s1s;
	char *s2 = calloc(250, sizeof(char)), *s2s;
	char *bin_trim;
	char *orgs;
	s1s = s1;
	s2s = s2;
	orgs = org;
	int k = 0, t;

	for (; *org != '\0'; *org++) {
		if (*org - 48 > 0) {
			bin_trim = bin(*org - 48);
			k = strlen(bin_trim);
			if (k > 1) {
				t = k - 1;
				while (t-- != 0) {
					*s1++ = '0';
				}
				*s1++ = '1';
				s1 = s1s;
				sprintf(s1, "%s%s", s1, bin_trim);
			} else if (k == 1) {
				sprintf(s1, "%d%d", 1, 1);
			}

			free(bin_trim);
			bin_trim = NULL;
		} 
		else 
			sprintf(s1, "%d%d", 1, 0);
		sprintf(s2, "%s%s", s2, s1);
		s1 = s1s;
		memset(s1, '\0', 50);
	}
	s1 = s1s;
	s2 = s2s;
	org = orgs;
	free(s1); s1 = NULL;
	return s2;
}

char *decode(const char *org)
{
	char *s = calloc(250, sizeof(char)), *sp;
	char *t = calloc(250, sizeof(char)), *tp, *orgp;
	sp = s;
	tp = s;
	orgp = org;
	int i = 0;
	int bin_index = 0;
	int len = strlen(org);
	if (len < 1) return s;
	for (;*org != '\0';) {
		if (*org == 49) {
			if (bin_index == 0) { 
				*(org + 1) == 48 ? sprintf(s, "%s%c", s, 48) : sprintf(s, "%s%c",s, 49);
				*org++; *org++;
				bin_index = 0;
			} else {
				*org++;
				bin_index++;
			}
		} else if (*org == 48) { 	
			if (bin_index == 0) {	
				if (*(org + 1) == 49) { 
					if (*(org + 3) == 48) {
						sprintf(s, "%s%c",s, 50);
						*org++; *org++; *org++; *org++;
						bin_index = 0;
					} else {
						sprintf(s, "%s%c", s, 51);
						*org++; *org++; *org++; *org++;
						bin_index = 0;
					}
				} else if (*(org + 1) == 48) { 
					if (*(org + 2) == 49) { 
						if (*(org + 4) == 48) { 
							if (*(org + 5) == 48) { 
								sprintf(s, "%s%c", s, 52);
								*org++; *org++; *org++; *org++;
								*org++; *org++;
								bin_index = 0;
							} else {
								sprintf(s, "%s%c", s, 53);
								*org++; *org++; *org++; *org++;
								*org++; *org++;
								bin_index = 0;
							}
						} else if (*(org + 4) == 49) {
								if (*(org + 5) == 48) {
									sprintf(s, "%s%c", s, 54);
									*org++; *org++; *org++; *org++;
									*org++; *org++;
									bin_index = 0;
								} else {
									sprintf(s, "%s%c", s, 55);
									*org++; *org++;
									*org++; *org++;
									*org++; *org++;
									bin_index = 0;
								}
						}
					} else if (*(org + 2) == 48) {
						if (*(org + 7) == 49) {
							sprintf(s, "%s%c", s, 57);
							*org++; *org++; *org++; *org++;
							*org++; *org++; *org++; *org++;
							bin_index = 0;
						} else {
							sprintf(s, "%s%c", s, 56);
							*org++; *org++; *org++; *org++;
							*org++; *org++; *org++; *org++;
							bin_index = 0;
						}
					}
				}
			}

		} else {
			*org++;
			bin_index++;
		}
	}
	org = orgp;
	s = tp;
	free(t); t = NULL;
	return s;
}

int main(void)
{
	/*
	int i = 0;
	char s[4];
	for (; i < 10; i++) {
		sprintf(s, "%d", i);
		printf("code(%d) --> %s\n", i, code(s));
	}
	*/

	char *a = decode("10");
	printf("10:%s\n", a);
	free(a); a = NULL;

	char *b = decode("11");
	printf("11:%s\n", b);
	free(b); b = NULL;

	char *c = decode("01101000110111001100011011");
	printf("2051421:%s\n", c);
	free(c); c = NULL;

	char *d = decode("001111001111011101110001100000011000001101001101");
	printf("77338855:%s\n", d);
	free(d); d = NULL;

	/* code(0) --> 10
	* code(1) --> 11
	* code(2) --> 0110
	* code(3) --> 0111
	* code(4) --> 001100
	* code(5) --> 001101
	* code(6) --> 001110
	* code(7) --> 001111
	* code(8) --> 00011000
	* code(9) --> 00011001
	*
	*/


	
	//printf("%s\n", code("77338855"));
	//printf("%s\n", code("77338"));
	//printf("%s\n", code("0011121314"));
	return 0;
}
