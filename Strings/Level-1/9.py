# Print the ASCII value of each character in a string.

# 1. ord(char): Converts a single character into its corresponding 
# integer Unicode/ASCII value.

# 2. chr(integer): The opposite function. If you ever need to 
# convert an ASCII number back into a text character, 
# use chr(). For example, chr(72) will return 'H'

str1 = "Rohan"

for str in str1:
    print(f"{str}-> ASCII: ",ord(str))


word = 82

print(f"\n{word}->Letter: ",chr(word))

