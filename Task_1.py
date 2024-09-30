# Function to encrypt text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Leave non-alphabetical characters unchanged
        else:
            result += char
    return result

# Function to decrypt text using Caesar Cipher
def decrypt(text, shift):
    result = ""
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        # Leave non-alphabetical characters unchanged
        else:
            result += char
    return result

# Main program
def caesar_cipher():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'encrypt':
        print("Encrypted message:", encrypt(message, shift))
    elif choice == 'decrypt':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

# Run the program
if __name__ == "__main__":
    caesar_cipher()
