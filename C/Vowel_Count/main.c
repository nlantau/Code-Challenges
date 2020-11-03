#include <stddef.h>

size_t get_count(const char *s)
{
  size_t counter = 0;
  while(*s)
  {
    if (*s == 'a' || *s == 'e' || *s == 'i' || *s == 'o' || *s == 'u') counter++;
    *s++;

  }
  return counter;

}
