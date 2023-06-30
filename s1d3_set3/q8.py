def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    return word_count

input_file = "input.txt"
output_file = "output.txt"

# Count the number of words in the input file
num_words = count_words(input_file)

# Write the count to the output file
with open(output_file, 'w') as file:
    file.write("Number of words: {}".format(num_words))

print("Count written to output file successfully!")
