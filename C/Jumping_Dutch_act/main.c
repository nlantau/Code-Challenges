/* Completed */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * sc(int n)
{
  char * none_e = "";
  char * none = malloc (1);
  strcpy(none, none_e);

  char * scream = "Aa~";
  char * ass_to_grass = "Pa!";
  char * you_dead = "Aa!";

  if (n == 1) return none;
  if (n < 1) return none;

  char * ret = malloc (strlen (scream) * n + n);
  strcpy(ret, scream);


  if (n < 7)
  {

    while(--n > 1)
    {
      strcat(ret, " ");
      strcat(ret, scream);
    }
    strcat(ret, " ");
    strcat(ret, ass_to_grass);
    strcat(ret, " ");
    strcat(ret, you_dead);
    
    return ret;
  }
  else if (n >= 7)
  {
    while(--n > 1)
    {
      strcat(ret, " ");
      strcat(ret, scream);
    }
    strcat(ret, " ");
    strcat(ret, ass_to_grass);
    
    return ret;
  }
  return none;
}
/*
int main(void)
{

  printf("%s\n", sc(2));
  printf("%s\n", sc(6));
  printf("%s\n", sc(7));
  printf("%s\n", sc(10));
  printf("%s\n", sc(1));
  printf("%s\n", sc(-1));

  return 0;
}
*/
