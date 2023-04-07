#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);
void convert(int n, int b);

int main(void)
{
    // TODO
    string message = get_string("Message: ");

    for (int i = 0; message[i] != '\0'; i++)
    {
        int n = (int) message[i];
        convert(n, BITS_IN_BYTE);
        printf("\n");
    }

}

void convert(int n, int b)
{
    if (b == 0)
    {
        return;
    }
    int r = n % 2;
    n /= 2;
    convert(n, b - 1);
    print_bulb(r);
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
