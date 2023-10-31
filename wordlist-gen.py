import itertools

# Function to generate a wordlist
def wordlist_gen(characters, min_length, max_length):
    wordlist = []
    total_combinations = 0
    
    for length in range(min_length, max_length + 1):
        combinations = itertools.product(characters, repeat=length)
        for combination in combinations:
            word = ''.join(combination)
            wordlist.append(word)
            total_combinations += 1
            
    return wordlist, total_combinations

# Prompt user for input
characters = input("Enter characters (comma-separated eg a,b,0,1): ").replace(" ", "")
min_length = int(input("Enter minimum word length: "))
max_length = int(input("Enter maximum word length: "))

# Convert characters string to a list
characters = characters.split(',')

wordlist, total_combinations = wordlist_gen(characters, min_length, max_length)

# Prompt user for output file name
output_file = input("Enter output file name: ")

# Write wordlist to file
with open(output_file, 'w') as file:
	file.write('\n'.join(wordlist))

print("\n")
print("Wordlist generated successfully")
print("Wordlist has been saved as", output_file)
print("Total combinations generated:", total_combinations)


