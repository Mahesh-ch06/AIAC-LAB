#Write a Python code to creates a file named 'sample.txt', writes three lines of example text to it, then reads the file back and prints the content to the console.

def main() -> None:
    file_name = 'sample.txt'
    
    # Writing to the file
    with open(file_name, 'w') as file:
        file.write("This is the first line of example text.\n")
        file.write("This is the second line of example text.\n")
        file.write("This is the third line of example text.\n")
    
    # Reading from the file
    with open(file_name, 'r') as file:
        content = file.read()
    
    # Printing the content to the console
    print("Content of 'sample.txt':")
    print(content)
if __name__ == "__main__":
    main()
    