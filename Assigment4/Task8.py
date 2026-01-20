# Generate a list of words.
words = ["level", "world", "radar", "python", "civic", "java", "deified", "code", "rotor", "script"]
# Calculate length of each word
for word in words:
    length = len(word)  # Calculate the length of the word
    print(f"The length of the word '{word}' is {length}.")  # Print the word and its length
# Classify words as Short or Long
    if length < 5:
        print(f"'{word}' is a Short word.")  # Print if the word is short
    else:
        print(f"'{word}' is a Long word.")  # Print if the word is long
    print()  # Print a newline for better readability
