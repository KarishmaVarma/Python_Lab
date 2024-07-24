#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

def read_and_display_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  # end='' prevents adding an extra newline
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")

# Usage
read_and_display_file('ABC.txt')

#Output:
#hello, how are you
