def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            if decrypt:
                shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
operation = input("Encrypt or Decrypt? (e/d): ").lower()

if operation == "e":
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
elif operation == "d":
    decrypted_text = caesar_cipher(text, shift, decrypt=True)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid operation. Please choose 'e' for encryption or 'd' for decryption.")
