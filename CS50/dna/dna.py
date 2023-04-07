import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print('Incorrect input! Usage: python dna.py csv_file txt_file')
        return 1

    # TODO: Read database file into a variable

    # Ok, lets create an empty list of dictionaries
    data = []

    # Now, lets start reading the file
    with open(sys.argv[1], 'r') as file:
        # Create reader
        reader = csv.DictReader(file)

        # Take a list of keys
        key_list = reader.fieldnames

        # Start reading row by row and add it in database
        for row in reader:
            for i in range(1, len(key_list)):
                row[key_list[i]] = int(row[key_list[i]])
            data.append(row)

    # TODO: Read DNA sequence file into a variable
    # Lets open and read txt file
    with open(sys.argv[2], 'r') as text:
        sequence = text.readline()

    # TODO: Find longest match of each STR in DNA sequence
    match = []
    for i in range(1, len(key_list)):
        match.append(longest_match(sequence, key_list[i]))

    # TODO: Check database for matching profiles
    for item in data:
        found = True
        for i in range(1, len(key_list)):
            if (item[key_list[i]] != match[i - 1]):
                found = False
        if (found):
            print(item[key_list[0]])
            return
    if (found == False):
        print('No match')


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
