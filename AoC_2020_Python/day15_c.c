#include <stdio.h>
#include <string.h>

//#define SIZE 30000000
#define SIZE 9

int main(void)
{
    int arr[SIZE];
    memset(arr, 99999999, SIZE * sizeof(arr[0]));
    arr[0] = 0;
    arr[1] = 3;
    arr[2] = 6;
    //arr[3] = 12;
    //arr[4] = 1;
    //arr[5] = 3;

    for (int i = 2; i < SIZE - 1; i++)
    {
        int spoken_in_arr = 0;
        int num = 0;
        int index = 0;
        int prev_index = i + 1;
        int spoken = arr[i];
        printf("prev %d, spoken %d\n", prev_index, spoken);
        for (int k = 0; k < SIZE - 2; k++)
        {
            if (spoken == arr[k])
            {
                spoken_in_arr = 1;
            }
        }
        if (spoken_in_arr == 1)
        {
            for (int x = 0; x < SIZE - 3; x++)
            {
                if (spoken == arr[x])
                {
                    index = x + 1;
                    printf("index: %d\n", index);
                }
            }
            num = prev_index - index;
            arr[i + 1] = num;
        }
        else
        {
            arr[i + 1] = 0;
        }
        int p = 0;
        while (p < SIZE - 1)
        {
            printf("%d, ", arr[p++]);
        }
        printf("\n");
    }
    printf("%d\n", arr[SIZE - 1]);
}