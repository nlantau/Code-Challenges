#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct {
  char digit;
  char *coded;
  int length;
} convert[] = { {'0', "10", 2}, {'1', "11", 2}, {'2', "0110", 4}, {'3', "0111", 4}, {'4', "001100", 6}, {'5', "001101", 6},\
{'6', "001110", 6}, {'7', "001111", 6}, {'8', "00011000", 8}, {'9', "00011001", 8}};

char* code(const char* strng){
  char *coded = (char *) malloc(8 * sizeof(char) * strlen(strng));
  *coded = '\0';
  
  for (; *strng != '\0'; strng++)
    strcat(coded, convert[*strng-'0'].coded);
    
  return coded;
}

char* decode(const char* str){
  const char *ptr = str;
  char *decoded = (char *) malloc(strlen(str) * sizeof(char));
  *decoded = '\0';
  
  while (*ptr != '\0')  
    for (int i = 0; i < 10; i++)
      if (ptr == strstr(ptr, convert[i].coded)) {
        strcat(decoded, &convert[i].digit);
        ptr += convert[i].length;break;
      }
  
  return decoded;
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
