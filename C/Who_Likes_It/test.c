#include <criterion/criterion.h>
#include <stddef.h>

char* likes(size_t n, const char *const names[n]);

Test(Sample_Tests, should_pass_all_the_tests_provided) {
  {
    const char *const names[0] = {};
    char* expected = "no one likes this";
    char* submitted = likes(0, names);
    cr_assert_str_eq(expected, submitted,
        "Expected : %s\nSubmitted: %s\n\n", expected, submitted);
    free(submitted); submitted = NULL;
  }
  {
    const char *const names[1] = {"Peter"};
    char* expected = "Peter likes this";
    char* submitted = likes(1, names);
    cr_assert_str_eq(expected, submitted,
        "Expected : %s\nSubmitted: %s\n\n", expected, submitted);
    free(submitted); submitted = NULL;
  }
  {
    const char *const names[2] = {"Jacob", "Alex"};
    char* expected = "Jacob and Alex like this";
    char* submitted = likes(2, names);
    cr_assert_str_eq(expected, submitted,
        "Expected : %s\nSubmitted: %s\n\n", expected, submitted);
    free(submitted); submitted = NULL;
  }
  {
    const char *const names[3] = {"Max", "John", "Mark"};
    char* expected = "Max, John and Mark like this";
    char* submitted = likes(3, names);
    cr_assert_str_eq(expected, submitted,
        "Expected : %s\nSubmitted: %s\n\n", expected, submitted);
    free(submitted); submitted = NULL;
  }
  {
    const char *const names[4] = {"Alex", "Jacob", "Mark", "Max"};
    char* expected = "Alex, Jacob and 2 others like this";
    char* submitted = likes(4, names);
    cr_assert_str_eq(expected, submitted,
        "Expected : %s\nSubmitted: %s\n\n", expected, submitted);
    free(submitted); submitted = NULL;
 }
}
