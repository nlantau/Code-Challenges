#include <criterion/criterion.h>
int multiply(int, int);

Test(ExampleTests, should_pass_all_the_tests_provided) {
    cr_assert_eq(multiply(5, 6), 30);
    cr_assert_eq(multiply(12, 12), 144);
}
