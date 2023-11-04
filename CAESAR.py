def caesar_cipher(message, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.
    Args:
    - message (str): the message to be encrypted or decrypted
    - shift (int): the amount to shift each letter by
    - mode (str): the mode of operation, either 'encrypt' or 'decrypt'
    Returns:
    - str: the encrypted or decrypted message
    """
    # Convert the message to lowercase.
    message = message.lower()
    # Create a new string to hold the result.
    result = ""
    # Loop through the message characters.
    for character in message:
        # If the character is a letter, encrypt or decrypt it.
        if character.isalpha():
            # Get the shifted letter by adding or subtracting the shift amount.
            if mode == 'encrypt':
                shifted_letter = chr((ord(character) - ord('a') + shift) % 26 + ord('a'))
            elif mode == 'decrypt':
                shifted_letter = chr((ord(character) - ord('a') - shift) % 26 + ord('a'))
            else:
                raise ValueError("Invalid mode, must be 'encrypt' or 'decrypt'")
            # Add the shifted letter to the result.
            result += shifted_letter
        # Otherwise, just add the character to the result.
        else:
            result += character
    return result

# Get the input message from the user.
message = input("Enter message: ")
# Get the shift amount from the user.
shift = int(input("Enter shift amount: "))
# Get the mode of operation from the user.
mode = input("Enter operation (encrypt/decrypt): ")
# Encrypt or decrypt the message using the Caesar Cipher algorithm.
if mode == 'encrypt':
    result = caesar_cipher(message, shift, 'encrypt')
    print("The encrypted message is:", result)
elif mode == 'decrypt':
    result = caesar_cipher(message, shift, 'decrypt')
    print("The decrypted message is:", result)
else:
    print("Invalid mode, must be 'encrypt' or 'decrypt'")
