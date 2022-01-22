#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char *likes(size_t n, const char *const names[n])
{
    char *no_one = "no one likes this";

    char *one_like = " likes this";
    char *two_like2 =  " like this";
    char *and = " and ";
    char *comma = ", ";
    char _buf[2]; 
    char *more = " others like this";

    char *ret = malloc(sizeof(char) * 50);

    switch (n)
    {
    case 0:
        strcpy(ret, no_one);
        return ret;
        break;
    case 1:
        strcpy(ret, *names);
        strcat(ret, one_like);
        return ret;
        break;
    case 2:
        strcpy(ret, *names++);
        strcat(ret, and);
        strcat(ret, *names);
        strcat(ret, two_like2);
        return ret;
        break;
    case 3:
        strcpy(ret, *names++);
        strcat(ret, comma);
        strcat(ret, *names++);
        strcat(ret, and);
        strcat(ret, *names);
        strcat(ret, two_like2);
        return ret;
    case 4 ... 100:
        strcpy(ret, *names++);
        strcat(ret, comma);
        strcat(ret, *names++);
        strcat(ret, and);
        sprintf(_buf, "%zu", (n-2));
        strcat(ret, _buf);
        strcat(ret, more);

        return ret;
    }
    return NULL;
}
#if 0
int main(void)
{
    //const char *const names[1] = {"Peter"};
    const char *const names[4] = {"Alex", "Jacob", "Mark", "Max"};
    char *submitted = likes(0, names);

    printf("%s\n", submitted);
    free(submitted);
}
#endif