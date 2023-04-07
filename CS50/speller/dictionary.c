// Implements a dictionary's functionality

#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int count = 0;
int hash_value = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

void free_node(node *cursor);

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // So now we have the word
    // Lets see where it belongs to
    hash_value = hash(word);

    // Set cursor to first table value
    node *cursor = table[hash_value];

    // Start cycle untill it reaches NULL
    while (cursor != NULL)
    {
        // If you find the word return true
        if (strcasecmp(word, cursor -> word) == 0)
        {
            return true;
        }

        // If not, go to next node
        cursor = cursor -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        sum += tolower(word[i]);
    }
    sum += strlen(word) - 1;

    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open then file
    FILE *dict = fopen(dictionary, "r");

    // Check if it's opened
    if (dict == NULL)
    {
        return false;
    }

    // Start reading from dictionary
    char buffer[LENGTH + 1];
    while (fscanf(dict, "%s", buffer) != EOF)
    {
        hash_value = hash(buffer);
        node *new_node = malloc(sizeof(node));
        // Check if memory allocated
        if (new_node == NULL)
        {
            return false;
        }

        // Put new word in hash table
        strcpy(new_node -> word, buffer);
        new_node -> next = table[hash_value];
        table[hash_value] = new_node;
        count++;
    }
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Just return count
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // So we need to free up the whole hash table
    for (int i = 0; i < N; i++)
    {
        free_node(table[i]);
    }
    return true;
}

void free_node(node *cursor)
{
    // This is the base case
    if (cursor == NULL)
    {
        return;
    }

    free_node(cursor -> next);

    // Free the head
    free(cursor);
}
