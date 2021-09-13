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
void print_struct(cfreq *s, cfreq *t);

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

	typedef struct {
		char chr;
		int length;
	} c_table;

	c_table c_t[2];
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
			printf("ss1[%d].dig = [%d]\n", i, ss1[i].dig);
			printf("ss2[%d].dig = [%d]\n", i, ss2[i].dig);


			for (int j = 0; j < ss1[i].dig; j++) {
				*s1ct++ = ss1[i].chr;
				printf("*s1ct = [%s]\n", s1ctp);
			}
			for (int j = 0; j < ss2[i].dig; j++)
				*s2ct++ = ss2[i].chr;
				printf("*s2ct = [%s]\n", s1ctp);
			//printf("s1ct = [%s]\n", s1ct);
			//printf("s2ct = [%s]\n", s2ct);

			//printf("len: s1ct=[%d], s2ct[%d]\n",\
					strlen(s1ct), strlen(s2ct));

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
	printf("s1c  = [%s]\n", s1cp);
	printf("s1c  = [%s]\n", s1c);
	printf("s1ct = [%s]\n", s1ctp);
	printf("s2ct = [%s]\n", s2ctp);
	free(s1ctp); s1ctp = NULL;
	free(s2ctp); s2ctp = NULL;
	
	return s1cp;
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
