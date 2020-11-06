#include <criterion/criterion.h>
#include <stdbool.h>

bool array_madness(size_t n1, const int arr1[n1], size_t n2, const int arr2[n2]);
void tester(size_t n1, const int arr1[n1], size_t n2, const int arr2[n2], bool expected);

Test(Example_Tests, should_pass_all_the_tests_provided) {
  {
    const int arr1[3] = {4, 5, 6};
    const int arr2[3] = {1, 2, 3};
    tester(3, arr1, 3, arr2, true);
  }
  {
    const int arr1[3] = {1, 2, 3};
    const int arr2[3] = {4, 5, 6};
    tester(3, arr1, 3, arr2, false);
  } 
}