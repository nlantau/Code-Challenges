#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <math.h>

bool array_madness(size_t n1, const int arr1[], size_t n2, const int arr2[])
{
    double arr_1_res = 0.0;
    double arr_2_res = 0.0;

    for (uint8_t i = 0; i < n1; i++)
    {
        arr_1_res += pow(arr1[i], 2);
    }

    for (uint8_t i = 0; i < n2; i++)
    {
        arr_2_res += pow(arr2[i], 3);
    }
    return arr_1_res > arr_2_res;
}