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

typedef struct {
	char num_or_sign;
	char chr;
	int len;
} c_table;

char* mix(char* s1, char* s2);
void print_struct(cfreq *s, cfreq *t);
void print_ctable(c_table *s);

int main(void)
{
	char *s1 = "my&friend&Paul has heavy hats! &";
	char *s2 = "my friend John has many many friends &";


	//s1 = "A aaaa bb c";


	char *s3 = mix(s1,s2);
	printf("-> [%s]\n", s3);

	free(s3); s3 = NULL;
	return 0;
}

char* mix(char* s1, char* s2)
{


	char *ps1 = s1, *ps2 = s2;
	cfreq ss1[26];
	cfreq ss2[26];
	for (int i = 0; i < 26; i++) {
		ss1[i].dig = 0;
		ss2[i].dig = 0;
	}


	// Count frequency
	for (char a = 'a', i = 0; a <= 'z'; a++, i++) {
		ss1[i].chr = a;
		ss2[i].chr = a;
		while(*s1) 
			if (*s1++ == a)
				ss1[i].dig++; 
		while(*s2) 
			if (*s2++ == a)
				ss2[i].dig++; 
		s1 = ps1;
		s2 = ps2;
	}

	print_struct(ss1, ss2);

	// combine struct data to a string
	char *s1c = calloc(1, 100), *s1cp = s1c;

	char *s1ct = calloc(1, 100), *s1ctp = s1ct; // *s1 count temp
	char *s2ct = calloc(1, 100), *s2ctp = s2ct; // *s2 count temp


	for (int i = 0; i < 26; i++) {

		// Only 'strictly greater than 1 is interesting
		if (ss1[i].dig > 1 || ss2[i].dig > 1) {

			for (int j = 0; j < ss1[i].dig; j++)
				*s1ct++ = ss1[i].chr;
			for (int j = 0; j < ss2[i].dig; j++)
				*s2ct++ = ss2[i].chr;

			s1ct = s1ctp;
			s2ct = s2ctp;
			if (strlen(s1ct) > strlen(s2ct)) {
				strcat(s1c, "1:");
				strcat(s1c, s1ct);
				strcat(s1c, "/");
				//sprintf(s1c, "%s1:%s/",s1c, s1ct);
			} else if (strlen(s1ct) < strlen(s2ct)) {
				strcat(s1c, "2:");
				strcat(s1c, s2ct);
				strcat(s1c, "/");
				//sprintf(s1c, "%s2:%s/",s1c, s2ct);
			} else if (strlen(s1ct) == strlen(s2ct)) {
				strcat(s1c, "=:");
				strcat(s1c, s2ct);
				strcat(s1c, "/");
				//sprintf(s1c, "%s=:%s/",s1c, s2ct);
			}

			memset(s1ct, '\0', 100);
			memset(s2ct, '\0', 100);

		}
	}

	s1ct = s1ctp;
	s2ct = s2ctp;

	// String count thing is complete
	// Now - need to put in correct order
	
	// s1c is our string.
	//s1cp = s1c;
	
	printf("s1c  = [%s]\n", s1cp);
	printf("s1c  = [%s]\n", s1c);
	
	c_table c_o[26];

	/* c_o[0].num_or_sign = '1', '2' or '='
	 * c_o[0].chr         = 'a' -> 'z'
	 * c_o[0].len         = number of letters until '/'
	 */

	for (int i = 0; i < 26, *s1c != '\0'; i++) {
		//printf("*s1c = [%c]\n", *s1c);
		c_o[i].num_or_sign = *s1c;
		c_o[i].chr = *(s1c +2);
		c_o[i].len = 1;
		while(*s1c == *(s1c+1)) {
			c_o[i].len++;
			*s1c++;
		}
		c_o[i].len++;
	}
	print_ctable(c_o);

	s1c = s1cp;
	printf("s1c  = [%s]\n", s1cp);
	printf("s1c  = [%s]\n", s1c);
	printf("s1ct = [%s]\n", s1ctp);
	printf("s2ct = [%s]\n", s2ctp);
	free(s1ct); s1ct = NULL;
	free(s2ct); s2ct = NULL;
	
	return s1cp;
}

void print_ctable(c_table *s)
{
	for (int i = 0; i < 26; i++) {
		printf("c_o[%2d].nos = [%2c] | c_o[%2d]."
		       "chr = [%2c] | c_o[%2d].len = [%2d]\n", 
		       i, s[i].num_or_sign,
		       i, s[i].chr, i, s[i].len);
	}
}

void print_struct(cfreq *s, cfreq *t)
{
	for (int i = 0; i < 26; i++)
		printf("ss1[%2d].chr = [%2c]\tss1[%2d].dig = [%2d]\n",\
				i, s[i].chr, i, s[i].dig);
	printf("<-------------------------->\n");
	for (int i = 0; i < 26; i++)
		printf("ss2[%2d].chr = [%2c]\tss2[%2d].dig = [%2d]\n",\
				i, t[i].chr, i, t[i].dig);
}
