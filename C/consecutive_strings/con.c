/* Consecutive Strings - 6 kyu
 * nlantau, 2021-09-12
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *longestConsec(char *sarr[], int n, int k);

int main(void)
{

	char* a1[] = {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
	// a1, 8, 2 --> "abigailtheta"
	
	char* b1[] = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
	// b1, 5, 1 --> "oocccffuucccjjjkkkjyyyeehh"
	
	char* arr[] = {"itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"};
	// arr, 3, 2 --> "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
	
	char* brr[] = {};
	// brr, 0, 3 --> ""

	char *s = longestConsec(a1, 8, 2);
	printf("[%s]\n", s);
	free(s); s = NULL;

	s = longestConsec(b1, 5, 1);
	printf("[%s]\n", s);
	free(s); s = NULL;

	s = longestConsec(arr, 3, 2);
	printf("[%s]\n", s);
	free(s); s = NULL;

	s = longestConsec(brr, 0, 3);
	printf("[%s]\n", s);
	free(s); s = NULL;

	s = longestConsec(arr, 3, 2);
	printf("[%s]\n", s);
	free(s); s = NULL;
	return 0;
}


char *longestConsec(char *sarr[], int n, int k)
{  

	int i = 0, j = 0, c = 1, csize = 0;
	char **t = NULL;
	char *s = calloc(1, sizeof(char));
	if ((n == 0) || (k > n) || (k <= 0)) {
		strcpy(s, "");
		return s;
	}
	for (; i < n; i++) {
		csize = 0;
		for (j = i; j != k+1 && j != n; j++) csize += strlen(sarr[j]);
		t = realloc(t, sizeof(char*) * ++c);
		t[i] = calloc(1, csize + 1);
		for (j = i; j != k+i && j != n; j++) strcat(t[i], sarr[j]);
		if (strlen(t[i]) > strlen(s)) {
			s = realloc(s, strlen(t[i]) * sizeof(char) );
			strcpy(s, t[i]);
		}
	}
	for (i = 0; i < n; i++) free(t[i]);
	free(t); t = NULL;
	return s;
}
