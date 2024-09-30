
def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
    
def decrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
       
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
       
        else:
            result += char
    return result

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

if __name__ == "__main__":
    caesar_cipher()
