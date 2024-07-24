#2. Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            word_count = 0
            for line in file:
                words = line.split()  # Split line into words
                word_count += len(words)  # Count words in the line

        print(f"Total number of words in {filename}: {word_count}")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: Could not read the file {filename}.")

# Usage
count_words_in_file('ABC.txt')

#Output:
#Total number of words in ABC.txt: 4
