# Function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to perform extended Euclidean algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to calculate modular inverse of a number 'a' mod 'm'
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

# Function to generate RSA keys
def generate_keys(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Check if e is coprime to phi
    if gcd(e, phi) != 1:
        raise ValueError("e is not coprime to phi")

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Function to generate digital signature
def digital_signature(private_key, message):
    d, n = private_key
    signature = pow(message, d, n)
    return signature

# Function to verify digital signature
def verify_signature(public_key, signature, message):
    e, n = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature

# Input values
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
e = int(input("Enter public key 'e': "))
M = int(input("Enter the message M: "))

# Key generation
public_key, private_key = generate_keys(p, q, e)
print("Public Key (e, n):", public_key)
print("Private Key (d, n):", private_key)

# Digital signature generation
signature = digital_signature(private_key, M)
print("Digital Signature:", signature)

# Signature verification
received_signature = int(input("Enter the received digital signature: "))
verified_message = verify_signature(public_key, received_signature, M)

# Display results
print("Verified Message M':", verified_message)
if verified_message == M:
    print("The message is authentic.")
else:
    print("Message is altered. Discard.")

