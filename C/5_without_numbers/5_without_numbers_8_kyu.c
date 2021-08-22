/* nlantau, 2021-08-23
 * 5 without numbers - 8 kyu
 */
#include <stdio.h>


int unusual_five(void) {
	//char a = 'A';
	//char d = 'D';
	//printf("a: %c -> %d\n", a, a);
	//return a ^ d;
	return 'A' ^ 'D';
}


int main(void) {
	int n = unusual_five();
	printf("n: %d\n", n);

	return 0;
}
