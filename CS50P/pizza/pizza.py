import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.csv'):
        with open(sys.argv[1], 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            print(tabulate(rows, headers="firstrow", tablefmt='grid'))
    else:
        raise sys.exit('Not a CSV file')
except Exception:
    sys.exit('File does not exist')