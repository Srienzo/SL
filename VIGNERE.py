def encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    plaintext = plaintext.upper().replace(" ", "")

    keyword_length = len(keyword)
    plaintext_length = len(plaintext)

    for i in range(plaintext_length):
        keyword_index = i % keyword_length
        keyword_char = keyword[keyword_index]
        keyword_ascii = ord(keyword_char) - 65

        plaintext_char = plaintext[i]
        plaintext_ascii = ord(plaintext_char) - 65

        encrypted_ascii = (plaintext_ascii + keyword_ascii) % 26
        encrypted_char = chr(encrypted_ascii + 65)
        ciphertext += encrypted_char

    return ciphertext

def decrypt(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()

    keyword_length = len(keyword)
    ciphertext_length = len(ciphertext)

    for i in range(ciphertext_length):
        keyword_index = i % keyword_length
        keyword_char = keyword[keyword_index]
        keyword_ascii = ord(keyword_char) - 65

        ciphertext_char = ciphertext[i]
        ciphertext_ascii = ord(ciphertext_char) - 65

        decrypted_ascii = (ciphertext_ascii - keyword_ascii) % 26
        decrypted_char = chr(decrypted_ascii + 65)
        plaintext += decrypted_char

    return plaintext

# Vigenère Table for reference
def generate_vigenere_table():
    table = [[0] * 26 for _ in range(26)]
    for row in range(26):
        for col in range(26):
            table[row][col] = chr((row + col) % 26 + ord('A'))
    return table

while True:
    print("Vigenère Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Vigenère Table")
    print("4. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        plaintext = input("Enter the plaintext: ")
        keyword = input("Enter the keyword: ")
        ciphertext = encrypt(plaintext, keyword)
        print("Ciphertext:", ciphertext)
    elif choice == "2":
        ciphertext = input("Enter the ciphertext: ")
        keyword = input("Enter the keyword: ")
        plaintext = decrypt(ciphertext, keyword)
        print("Decrypted plaintext:", plaintext)
    elif choice == "3":
        table = generate_vigenere_table()
        for row in table:
            print(" ".join(row))
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
