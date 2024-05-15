# Simple caesar cipher
# Accepts key int and plaintext string
# Returns ciphertext string
def caesar(key, plaintext):
    output = ""
    while key > 26: 
        key -= 26
    while key < 0:
        key += 26
    for character in plaintext:
        letter = character
        if character.isalpha():
            num = ord(character)
            num += key
            if num > 122:
                num -= 26
            elif num > 90 and num - key <=  90:
                num -= 26
            letter = chr(num)
        output = output + letter
    return output

# Converts key string to int array
# Accepts key string 
# Returns key int array
def key_to_int(key):
    key_array = []
    for character in key:
        key_array.append(ord(character))
    return key_array

# Shifts each char in plaintext based on key text
# Accepts key int array and plaintext string
# Returns ciphertext string
def char_shift(key_array, plaintext):
    output = ""
    increment = 0
    for character in plaintext:
        if increment >= len(key_array):
            increment = 0
        output = output + caesar(key_array[increment], character)
        increment += 1
    return output

# Changes key array to decrypt input text
# Accepts key int array
# Returns shifted key int array
def decrypt_key(key_array):
    output = []
    for num in key_array:
        output.append(26 - num)
    return output

# Get user input
print("Key: ", end="")
key_input = input()
print ("Input Text: ", end="")
string_input = input()
print ("Encrypt (0) or Decrypt (1): ", end="")
en_or_de = int(input())

# Encrypt text
if en_or_de == 0:
    output = char_shift(key_to_int(key_input), string_input)
    print("Ciphertext: ", output)
# Decrypt text
elif en_or_de == 1:
    output = char_shift(decrypt_key(key_to_int(key_input)), string_input)
    print("Plaintext: ", output)
# Not a valid input
else:
    print("Invalid Input")
