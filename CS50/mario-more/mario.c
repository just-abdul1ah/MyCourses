#include <cs50.h>
#include <stdio.h>

void makePyramid(int n, int x);

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (8 < n || n < 1);

    int x = n;

    makePyramid(n, x);

    return 0;
}

void makePyramid(int n, int x)
{
    if (n == 0)
    {
        return;
    }


    makePyramid(n - 1, x);

    for (int t = x; t > n; t--)
    {
        printf(" ");
    }

    for (int t = 0; t < n; t++)
    {
        printf("#");
    }

    printf("  ");

    for (int t = 0; t < n; t++)
    {
        printf("#");
    }

    printf("\n");

}