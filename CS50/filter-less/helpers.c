#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double a = image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed;
            a /= 3;
            int v = round(a);
            image[i][j].rgbtBlue = v;
            image[i][j].rgbtGreen = v;
            image[i][j].rgbtRed = v;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        typedef struct
        {
            int blue;
            int green;
            int red;
        }
        Triplet;
        Triplet triple[width];
        for (int j = 0; j < width; j++)
        {
            triple[j].blue = image[i][j].rgbtBlue;
            triple[j].green = image[i][j].rgbtGreen;
            triple[j].red = image[i][j].rgbtRed;
        }
        int z = 0;
        for (int k = width - 1; k > -1; k--)
        {
            image[i][z].rgbtBlue = triple[k].blue;
            image[i][z].rgbtGreen = triple[k].green;
            image[i][z].rgbtRed = triple[k].red;
            z++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j].rgbtBlue = image[i][j].rgbtBlue;
            copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            copy[i][j].rgbtRed = image[i][j].rgbtRed;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int n = 0;
            double red = 0;
            double green = 0;
            double blue = 0;
            if (i == 0 && j == 0)
            {
                red += copy[i][j + 1].rgbtRed + copy[i][j].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed;
                green += copy[i][j + 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen;
                blue += copy[i][j + 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue;
                n += 4;
            }
            else if (i > 0 && j > 0)
            {
                red += copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed;
                red += copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed;
                green += copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen;
                green += copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen;
                blue += copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue;
                blue += copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue;
                n += 4;
                if (i + 1 < height && j + 1 < width)
                {
                    red += copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed + copy[i][j + 1].rgbtRed + copy[i - 1][j +
                            1].rgbtRed;
                    green += copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen + copy[i][j + 1].rgbtGreen + copy[i
                             - 1][j + 1].rgbtGreen;
                    blue += copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i -
                            1][j + 1].rgbtBlue;
                    n += 5;
                }
                else if (j + 1 < width)
                {
                    red += copy[i][j + 1].rgbtRed + copy[i - 1][j + 1].rgbtRed;
                    green += copy[i][j + 1].rgbtGreen + copy[i - 1][j + 1].rgbtGreen;
                    blue += copy[i][j + 1].rgbtBlue + copy[i - 1][j + 1].rgbtBlue;
                    n += 2;
                }
                else if (i + 1 < height)
                {
                    red += copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed;
                    green += copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen;
                    blue += copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue;
                    n += 2;
                }
            }
            else if (j > 0)
            {
                red += copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed;
                green += copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen;
                blue += copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue;
                n += 4;
                if (j + 1 < width)
                {
                    red += copy[i][j + 1].rgbtRed + copy[i + 1][j + 1].rgbtRed;
                    green += copy[i][j + 1].rgbtGreen + copy[i + 1][j + 1].rgbtGreen;
                    blue += copy[i][j + 1].rgbtBlue + copy[i + 1][j + 1].rgbtBlue;
                    n += 2;
                }
            }
            else if (i > 0)
            {
                red += copy[i][j + 1].rgbtRed + copy[i][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i - 1][j].rgbtRed;
                green += copy[i][j + 1].rgbtGreen + copy[i][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen + copy[i - 1][j].rgbtGreen;
                blue += copy[i][j + 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue + copy[i - 1][j].rgbtBlue;
                n += 4;
                if (i + 1 < height)
                {
                    red += copy[i + 1][j + 1].rgbtRed + copy[i + 1][j].rgbtRed;
                    green += copy[i + 1][j + 1].rgbtGreen + copy[i + 1][j].rgbtGreen;
                    blue += copy[i + 1][j + 1].rgbtBlue + copy[i + 1][j].rgbtBlue;
                    n += 2;
                }
            }
            int aRed = round(red / n);
            int aGreen = round(green / n);
            int aBlue = round(blue / n);
            image[i][j].rgbtBlue = aBlue;
            image[i][j].rgbtGreen = aGreen;
            image[i][j].rgbtRed = aRed;
        }
    }
    return;
}
