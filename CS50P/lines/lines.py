import sys

try:
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.py'):
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
            bugs = []
            for line in lines:
                if str(line).strip().startswith('#'):
                    bugs.append(line)
                elif str(line).isspace():
                    bugs.append(line)
            for bug in bugs:
                lines.remove(bug)
            print(len(lines))
    else:
        raise sys.exit('Not a Python file')
except Exception:
    sys.exit('File does not exist')