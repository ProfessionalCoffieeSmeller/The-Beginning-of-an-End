filename = input("Enter the file name (with extension, e.g., 'sample.txt'): ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()               # Read all lines
        num_lines = len(lines)                 # Count number of lines
        num_words = sum(len(line.split()) for line in lines)  # Count words in all lines

    print(f"Total lines: {num_lines}")
    print(f"Total words: {num_words}")

except FileNotFoundError:
    print("Error: File not found. Please check the name and try again.")