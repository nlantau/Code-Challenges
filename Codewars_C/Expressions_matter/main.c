#include <stdio.h>

int expression_matter(int a, int b, int c)
{
    int d = a * (b + c);
    int e = a * b * c;
    int f = a + b * c;
    int g = (a + b) * c;
    int h = a + b + c;
    int i = a * b + c;

    int arr[] = {d, e, f, g, h, i};
    int temp = 0;

    for (int i = 0; i < 6; i++)
    {
        if (arr[i] > temp)
        {
            printf("%d\n", arr[i]);
            temp = arr[i];
        }
    }
    return temp;
}

int main(void)
{
    printf("%d\n", expression_matter(1, 1, 1));
}