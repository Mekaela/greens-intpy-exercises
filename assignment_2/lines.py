'''input: name (or path) of a Python file as command line argument,
output: number of lines of code in file, excluding comments and blank lines.
exceptions: !=1 command-line argument, name does not end in .py, file does not exist '''

# expects two command line arguments. e.g. python lines.py taqueria.py
import sys
import re

def main():
    try:
        check_command()
        with open(sys.argv[1]) as file:
            filtered_lines = remove_blank_lines(file)
            count = count_lines(filtered_lines)
            print(count)
    except FileNotFoundError:
        sys.exit('File not found')

def check_command():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def remove_blank_lines(file):
    # returns line, if not a blank line. strip removes empty spaces
    return (line for line in file if not re.match(r'^\s*$', line.strip()))

def count_lines(file):
    count = 0
    for line in file:
        # if comment, don't count
        line = line.strip()
        if line.startswith('#'):
            continue
        else:
            count+=1
    return count

main()