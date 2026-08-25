# Count how many characters (excluding spaces) are in the string

line = input("Enter a sentence: ")

char_count = len(line.replace(" ", ""))

print("Count of characters without spaces: ", char_count)