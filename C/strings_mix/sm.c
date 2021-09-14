/* Strings mix - 4 kyu
 * nlantau, 2021-09-13
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
	char chr;
	int dig;
} cfreq;

typedef struct {
	char nos;
	char chr;
	int len;
} c_table;

char* mix(char* s1, char* s2);
void print_struct(cfreq *s, cfreq *t);
void print_ctable(c_table *s);
int compare (const void* a, const void* b);

int main(void)
{
	char *s1 = "my&friend&Paul has heavy hats! &";
	char *s2 = "my friend John has many many friends &";


	//s1 = "A aaaa bb c";


	char *s3 = mix(s1,s2);
	printf("main -> [%s]\n", s3);

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

	//print_struct(ss1, ss2);

	// combine struct data to a string
	char *s1c = calloc(1, 100), *s1cp = s1c;

	char *s1ct = calloc(1, 100), *s1ctp = s1ct; // *s1 count temp
	char *s2ct = calloc(1, 100), *s2ctp = s2ct; // *s2 count temp

	char **tbone = NULL;

	int k = 0, ts = 2;
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
			} else if (strlen(s1ct) < strlen(s2ct)) {
				strcat(s1c, "2:");
				strcat(s1c, s2ct);
				strcat(s1c, "/");
			} else if (strlen(s1ct) == strlen(s2ct)) {
				strcat(s1c, "=:");
				strcat(s1c, s2ct);
				strcat(s1c, "/");
			}
			tbone = realloc(tbone, ++ts * sizeof(char*));
			tbone[k] = calloc(1, strlen(s1c) + 1);
			strcpy(tbone[k++], s1c);

			memset(s1c, '\0', 100);
			memset(s1ct, '\0', 100);
			memset(s2ct, '\0', 100);
		}
	}

	for (int i = 0; tbone[i] != '\0'; i++)
		printf("tbone[%2d] = [%9s], "
			"strlen(tbone[%2d]) = [%ld]\n",
			i, tbone[i], i, strlen(tbone[i]) );

	int nbr_of_strings = 0;
	int longest = 0;
	for (int i = 0; tbone[i] != '\0'; i++) {
		nbr_of_strings++;
		if (strlen(tbone[i]) > longest)
			longest = strlen(tbone[i]);
	}
	printf("-> longest        = [%d]\n", longest);
	printf("-> nbr_of_strings = [%d]\n", nbr_of_strings);
	printf("<---------------->\n\n");

	char *temp;

	for (int i = 0; i < nbr_of_strings; i++) {
		for (int j = 0; j < nbr_of_strings - i -1; j++) {
			if (strlen(tbone[j]) > strlen(tbone[j + 1])) {
				temp = tbone[j];
				tbone[j] = tbone[j + 1];
				tbone[j + 1] = temp;
			}
			else if (strlen(tbone[j]) == strlen(tbone[j + 1])) {
				if (tbone[i][0] != '=' && tbone[j][0] != '=') {
					if (tbone[j][2] < tbone[j+1][2]) {
					temp = tbone[j];
					tbone[j] = tbone[j + 1];
					tbone[j + 1] = temp;
					}
				}
				if (tbone[i][0] == '=' && tbone[j][0] == '=') {
					printf("--> i == '=' && j == '='\n");
					//printf("1ti: [%c], tj: [%c]\n", tbone[i][2], tbone[j][2]);
					//printf("1ti: [%c], tj: [%c]\n", tbone[i][0], tbone[j][0]);
					for (int x = 0; x < nbr_of_strings; x++) {
					if (tbone[x][2] > tbone[i][2]
					    && tbone[x][0] == '='
					    && tbone[i][0] == '=') {
						temp = tbone[i];
						tbone[i] = tbone[x];
						tbone[x] = temp;

						printf("tx: [%c], tj: [%c]\n", tbone[x][2], tbone[i][2]);
						printf("tx: [%c], tj: [%c]\n", tbone[x][0], tbone[i][0]);
					}

					}
				}
			}

		}
		printf("tbone[%2d][0] = [%c], "
			"tbone[%2d][2] = [%c]\n", 
			i, tbone[i][0], i, tbone[i][2]);
	}

	/* COMPLETED: Sorted by lenght
	 * TODO: Sort equally length strings by lexicographic order
	 *
	 *
	for (int i = 0; tbone[i] != '\0'; i++)
		printf("tbone[%2d] = [%9s], "
			"strlen(tbone[%2d]) = [%ld]\n",
			i, tbone[i], i, strlen(tbone[i]) );
	for (int i = 0; i < nbr_of_strings - 1 ; i++) {
		if (tbone[i][0] == '=') {
			for (int j=0; j < nbr_of_strings - i -1; j++) {
				if (tbone[j][0] == '=') {
					if (tbone[j][2] > tbone[i][2]) {
						temp = tbone[j];
						tbone[j] = tbone[i];
						tbone[i] = temp;

						printf("ti: [%c], tj: [%c]\n", tbone[i][2], tbone[j][2]);
						printf("ti: [%c], tj: [%c]\n", tbone[i][0], tbone[j][0]);
					}
				}
			}
		}
	}
	*/



	printf("\n\n<---------------->\n");
	
	printf("s1c  = [%s]\n", s1c);

	for (int i = 0; tbone[i] != '\0'; i++)
		printf("tbone[%2d] = [%9s], "
			"strlen(tbone[%2d]) = [%ld]\n",
			i, tbone[i], i, strlen(tbone[i]) );




	for (int i = 0; tbone[i] != '\0'; i++)
		free(tbone[i]);
	free(tbone); tbone = NULL;

	s1ct = s1ctp;
	s2ct = s2ctp;
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
		       i, s[i].nos,
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
