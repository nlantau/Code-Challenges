#include <criterion/criterion.h>
#include <string.h>

char* sc(int);

void dotest(int n, const char* expect)
{
  char* actual = sc(n);
  cr_expect(!strcmp(actual, expect), "Expected: '%s', got: '%s'\n", expect, actual);
  free(actual);
}

Test(the_multiply_function, should_pass_all_the_tests_provided) {
    dotest(2,"Aa~ Pa! Aa!");
    dotest(6, "Aa~ Aa~ Aa~ Aa~ Aa~ Pa! Aa!");
    dotest(7, "Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!");
    dotest(10, "Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Aa~ Pa!");
    dotest(1, "");
    dotest(-1, "");
}
