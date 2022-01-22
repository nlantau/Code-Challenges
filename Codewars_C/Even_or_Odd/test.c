#include <criterion/criterion.h>
#include <stdlib.h>

const char * even_or_odd(int number);

Test(ExampleTests, ShouldPassAllTheTestsProvided) {
  const int values[] = { 2, 1, 6, 21, 100 };
  const char * outputs[] = { "Even", "Odd", "Even", "Odd", "Even" };
  for (int index = 0; index < sizeof(values)/sizeof(values[0]); ++index) {
    char * expected = outputs[index];
    char * received = even_or_odd(values[index]);
    cr_assert_str_eq(expected, received, "Expected: %s Received: %s", expected, received);
  }
}
