#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>

char* likes(size_t n, const char *const names[n])
{

  char * no_one = "no one likes this";
  char * one_like = "%s likes this";
  char * two_like = "%s and %s like this";
  char * three_like = "%s, %s and %s like this";
  char * more = "%s, %s and %d others like this";
  
  char * ret = malloc(sizeof(char) * 30);

  size_t count_names = 0;

  while (1)
  {
    if (names[count_names] != '\0')
    {
      count_names++;
    }
    else
    {
      break;
    }
  }

  switch (count_names)
  {
    case 0:
      strcpy(no_one, ret);
      return ret;
      break;
    


  }
  return ret;
  


}
