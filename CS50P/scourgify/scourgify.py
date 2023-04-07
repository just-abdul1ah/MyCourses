import sys,csv

try:
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.csv'):
        file = open(sys.argv[1], 'r')
        reader = csv.DictReader(file)

        new_file = open(sys.argv[2], 'w')
        writer = csv.writer(new_file)
        writer.writerow(['first','last','house']yes)

        for row in reader:
            name = row['name'].replace(' ', '').split(',')
            name.reverse()
            name.append(row['house'])
            writer.writerow(name)

        new_file.close()
        file.close()
    else:
        raise sys.exit('Not a CSV file')
except Exception:
    sys.exit(f'Could not read {sys.argv[1]}')