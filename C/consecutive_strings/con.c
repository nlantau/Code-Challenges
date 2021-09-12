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

	char *s = longestConsec(a1, 8, 2);
	printf("[%s]\n", s);
	free(s); s = NULL;

	s = longestConsec(b1, 5, 1);
	printf("[%s]\n", s);
	free(s); s = NULL;

	s = longestConsec(arr, 3, 2);
	printf("[%s]\n", s);
	free(s); s = NULL;
	return 0;
}


char *longestConsec(char *sarr[], int n, int k)
{
	int i = 0, j = 0;
	char *t = calloc(100, sizeof(char));
	char *s = calloc(100, sizeof(char));

	for (; i < n; i++) {
		memset(t, '\0', strlen(t));
		for (j = i; j != k+i; j++) {
			t = realloc(t, strlen(sarr[j])* 100 * sizeof(char));
			strcat(t, sarr[j]);
		}
		printf("t = [%s]\n", t);
		if (strlen(t) > strlen(s)) {
			s = realloc(s, strlen(t) * sizeof(char) );
			memset(s, '\0', strlen(s));
			strcpy(s, t);
		}
	}

	free(t); t = NULL;
	return s;
}
